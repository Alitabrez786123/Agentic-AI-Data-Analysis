from smolagents import CodeAgent, OpenAIServerModel
from tools import (
    LoadCSVTool,
    DescribeDataTool,
    CleanColumnNamesTool,
    FilterAndSaveTool,
    GenerateSQLSchemaTool,
)


def create_agent():
    model = OpenAIServerModel(
        model_id="gpt-4.1-mini",  # or "gpt-4.1"
    )

    tools = [
        LoadCSVTool(),
        DescribeDataTool(),
        CleanColumnNamesTool(),
        FilterAndSaveTool(),
        GenerateSQLSchemaTool(),
    ]

    agent = CodeAgent(
        tools=tools,
        model=model,
        max_steps=10,
        add_base_tools=False,
    )
    return agent
