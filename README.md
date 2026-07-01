# 🤖 Autonomous AI Research Assistant Agent

An intelligent, tool-calling AI agent built using **LangChain** and **Anthropic's Claude** that automates the workflow of conducting background research, structuring findings into strict data formats, and saving compiled reports.

## 🚀 Features

* **Autonomous Researching:** Leverages Google/DuckDuckGo and Wikipedia to look up information dynamically based on user prompts[cite: 2, 4].
* **Strict Schema Outputs:** Uses `Pydantic` to parse raw LLM thoughts into a structured format containing the Topic, Summary, Sources, and Tools used[cite: 2].
* **Automated File Exports:** Includes a dedicated file-writing tool allowing the agent to save its research papers locally as timestamped text files[cite: 4].
* **State-of-the-Art Tool Calling:** Built on LangChain's native tool-calling agent architecture[cite: 2].

## 🛠️ Tech Stack

* **Framework:** LangChain (Core, Anthropic)[cite: 2, 3]
* **LLM Engine:** Anthropic Claude[cite: 2, 3]
* **Data Validation:** Pydantic[cite: 2, 3]
* **Search Tools:** DuckDuckGo Search API, Wikipedia API[cite: 3, 4]

## 📋 Project Structure

├── main.py            # Agent configuration, prompt engineering, and execution loop[cite: 2]

├── tools.py           # Implementation of custom search and file-saving tools[cite: 4]

├── requirements.txt   # Project dependencies[cite: 3]

└── .env               # API keys and environment variables (Do not commit to git!)
