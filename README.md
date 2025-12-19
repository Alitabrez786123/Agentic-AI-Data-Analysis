Agentic-AI-Data-Analysis
📌 Overview

The Agentic Data Analyst & ETL Automation Bot is an intelligent, tool-driven AI system built using Python, OpenAI, and smolagents. It is designed to autonomously perform common data analysis and ETL (Extract, Transform, Load) tasks by reasoning over user instructions and dynamically invoking the appropriate tools.

This project demonstrates how Agentic AI can be applied to real-world data engineering and analytics workflows, reducing manual effort and improving efficiency.

🚀 Key Features

📂 Load and manage multiple CSV datasets dynamically

🔍 Perform exploratory data analysis (EDA)

🧹 Clean and standardize column names for ETL readiness

✂️ Filter datasets using natural language instructions

🗄️ Generate SQL CREATE TABLE schemas automatically

🧠 Multi-step agentic reasoning using tool-based execution

⚙️ Modular and extensible architecture

🧠 Agentic AI Architecture

This project follows an Agent + Tools architecture:

LLM (OpenAI) acts as the reasoning engine

Custom Tools perform concrete actions (load CSV, clean data, filter, generate SQL)

Agent Controller (smolagents) plans, selects, and executes tools across multiple steps

The agent decides what to do next based on intermediate results, making it autonomous rather than script-driven.

🛠️ Tech Stack

Language: Python

Agent Framework: smolagents

LLM Provider: OpenAI

Data Processing: pandas

Environment Management: python-dotenv

IDE: Cursor

📂 Project Structure
agentic-data-analyst/
│── data/
│   ├── sales.csv
│   ├── customers.csv
│   ├── inventory.csv
│   └── orders.csv
│── tools.py          # Agent tools (ETL operations)
│── agent.py          # Agent definition
│── main.py           # CLI entrypoint
│── requirements.txt
│── README.md

▶️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/your-username/Agentic-AI-Data-Analysis.git
cd Agentic-AI-Data-Analysis

2️⃣ Create and Activate Virtual Environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set OpenAI API Key

Create a .env file:

OPENAI_API_KEY=your_api_key_here

5️⃣ Run the Agent
python main.py

🧪 Example Commands

Once the agent is running, try:

Load data/sales.csv as sales_data and describe it
Clean the column names for sales_data
Filter sales_data where total > 1000 and save to data/high_value_sales.csv
Generate a SQL schema based on sales_data

📈 Use Cases

Automated data cleaning for analytics teams

ETL pipeline prototyping

SQL schema generation for databases

Agentic AI demonstrations

Portfolio project for Data Engineering, AI, and ML roles

🔮 Future Enhancements

📊 Visualization tools (charts, plots)

🗄️ Database loaders (PostgreSQL / MySQL)

⏱️ Scheduled ETL jobs

☁️ Cloud integration (AWS / Azure)

🤖 Hugging Face model support

📜 License

This project is for educational and demonstration purposes. You are free to modify and extend it for learning or portfolio use.
