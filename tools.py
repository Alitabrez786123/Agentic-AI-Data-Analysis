import os
import pandas as pd
from smolagents import Tool

# Simple in-memory store for loaded DataFrames
DATA_CACHE = {}


class LoadCSVTool(Tool):
    name = "load_csv"
    description = (
        "Load a CSV file from a given path and store it in memory under a dataset name. "
        "Use this when the user wants to work with a specific CSV."
    )
    inputs = {
        "file_path": {
            "type": "string",
            "description": "Path to the CSV file on disk, e.g. 'data/sales.csv'.",
        },
        "dataset_name": {
            "type": "string",
            "description": "Name under which the dataset will be stored in memory.",
        },
    }
    output_type = "string"

    def forward(self, file_path: str, dataset_name: str) -> str:
        if not os.path.exists(file_path):
            return f"File not found: {file_path}"
        df = pd.read_csv(file_path)
        DATA_CACHE[dataset_name] = df
        return f"Loaded dataset '{dataset_name}' from '{file_path}' with shape {df.shape}."


class DescribeDataTool(Tool):
    name = "describe_data"
    description = (
        "Get high-level info and statistics for a dataset already loaded in memory. "
        "Use this to understand columns, types, nulls, shape, and basic stats."
    )
    inputs = {
        "dataset_name": {
            "type": "string",
            "description": "Name of the dataset previously loaded via load_csv.",
        }
    }
    output_type = "string"

    def forward(self, dataset_name: str) -> str:
        if dataset_name not in DATA_CACHE:
            return f"Dataset '{dataset_name}' not found. Load it first with load_csv."
        df = DATA_CACHE[dataset_name]

        info = {
            "columns": list(df.columns),
            "dtypes": df.dtypes.astype(str).to_dict(),
            "null_counts": df.isnull().sum().to_dict(),
            "shape": df.shape,
            "head": df.head(5).to_dict(orient="records"),
            "describe": df.describe(include="all").fillna("").to_dict(),
        }
        return str(info)


class CleanColumnNamesTool(Tool):
    name = "clean_column_names"
    description = (
        "Clean column names for a dataset: lowercased, stripped, and spaces replaced with underscores. "
        "Useful as a first step before SQL/ETL."
    )
    inputs = {
        "dataset_name": {
            "type": "string",
            "description": "Name of the dataset previously loaded in memory.",
        }
    }
    output_type = "string"

    def forward(self, dataset_name: str) -> str:
        if dataset_name not in DATA_CACHE:
            return f"Dataset '{dataset_name}' not found."
        df = DATA_CACHE[dataset_name]
        df.columns = (
            df.columns.astype(str)
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )
        DATA_CACHE[dataset_name] = df
        return f"Cleaned column names for dataset '{dataset_name}'. New columns: {list(df.columns)}"


class FilterAndSaveTool(Tool):
    name = "filter_and_save"
    description = (
        "Filter a dataset using a pandas-style query and save the result to a new CSV file. "
        "Use this when the user wants a subset of the data exported."
    )
    inputs = {
        "dataset_name": {
            "type": "string",
            "description": "Name of the dataset to filter.",
        },
        "query_str": {
            "type": "string",
            "description": "Pandas query string, e.g. 'Total > 1000 and Country == \"USA\"'.",
        },
        "output_path": {
            "type": "string",
            "description": "Path where the filtered CSV will be saved, e.g. 'data/high_value_sales.csv'.",
        },
    }
    output_type = "string"

    def forward(self, dataset_name: str, query_str: str, output_path: str) -> str:
        if dataset_name not in DATA_CACHE:
            return f"Dataset '{dataset_name}' not found."
        df = DATA_CACHE[dataset_name]
        try:
            filtered_df = df.query(query_str)
        except Exception as e:
            return f"Error applying query '{query_str}': {e}"
        filtered_df.to_csv(output_path, index=False)
        return (
            f"Saved filtered data from '{dataset_name}' ({filtered_df.shape[0]} rows) "
            f"to '{output_path}'."
        )


class GenerateSQLSchemaTool(Tool):
    name = "generate_sql_schema"
    description = (
        "Generate a SQL CREATE TABLE statement based on a dataset's columns and dtypes. "
        "Use this to prepare ETL table creation."
    )
    inputs = {
        "dataset_name": {
            "type": "string",
            "description": "Name of the dataset in memory.",
        }
    }
    output_type = "string"

    def forward(self, dataset_name: str) -> str:
        if dataset_name not in DATA_CACHE:
            return f"Dataset '{dataset_name}' not found."
        df = DATA_CACHE[dataset_name]

        type_map = {
            "int64": "INT",
            "float64": "FLOAT",
            "object": "TEXT",
            "bool": "BOOLEAN",
            "datetime64[ns]": "TIMESTAMP",
        }

        cols = []
        for col, dtype in df.dtypes.items():
            sql_type = type_map.get(str(dtype), "TEXT")
            safe_col = str(col).replace(" ", "_")
            cols.append(f"    {safe_col} {sql_type}")

        cols_str = ",\n".join(cols)
        create_stmt = f"CREATE TABLE my_table (\n{cols_str}\n);"
        return create_stmt
