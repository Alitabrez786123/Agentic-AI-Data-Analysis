import os
from dotenv import load_dotenv
from agent import create_agent

def main():
    load_dotenv()  # loads OPENAI_API_KEY if in .env

    agent = create_agent()

    print("=== Agentic Data Analyst & ETL Bot ===")
    print("Example tasks:")
    print("- 'Load data/sales.csv as sales_data and describe it'")
    print("- 'Clean the column names for sales_data'")
    print("- 'Filter sales_data where total > 1000 and save to data/high_value_sales.csv'")
    print("- 'Generate a SQL schema based on sales_data'")

    while True:
        user_input = input("\nEnter your request (or 'exit'): ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        try:
            result = agent.run(user_input)
            print("\n--- Agent Response ---")
            print(result)
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
