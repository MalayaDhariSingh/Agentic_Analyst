# 🏢 Enterprise Agentic News Analyst

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![CrewAI](https://img.shields.io/badge/AI-CrewAI-orange.svg)
![Llama 3.3](https://img.shields.io/badge/Model-Llama_3.3_70B-purple.svg)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red.svg)
![Docker](https://img.shields.io/badge/Deployment-Docker-blue.svg)

**An autonomous multi-agent system that plans, researches, drafts, and critiques executive briefings using Llama 3.3 and CrewAI.**

---

## 📖 Overview

This project demonstrates an **Agentic Workflow** where four distinct AI agents collaborate to produce high-quality research reports. Unlike simple "chatbots" that hallucinate facts, this system uses a **Planner-Executor-Reviewer** architecture to ensure accuracy and tonal consistency.

### 🤖 The Agent Team
1.  **🧠 Senior Strategist:** Analyzes the user's topic and creates a strategic research plan (identifies controversies, key players, and required data).
2.  **🕵️ Deep Researcher:** Executes the plan using **DuckDuckGo Search tools** to gather verified facts and real-time data.
3.  **✍️ Executive Communicator:** Synthesizes the research into a concise, C-Level briefing draft.
4.  **⚖️ Quality Control Board (Critic):** Reviews the draft for fluff, buzzwords, and hallucinations, forcing a rewrite if necessary.

---

## 🛠️ Tech Stack

* **Orchestration:** [CrewAI](https://www.crewai.com/) (Agent management & task delegation)
* **LLM Engine:** [Groq](https://groq.com/) running **Llama-3.3-70b-versatile** (High speed, zero cost)
* **Tools:** DuckDuckGo Search API (Internet access)
* **Frontend:** Streamlit (Reactive UI with real-time feedback)
* **Containerization:** Docker

---

## ⚡ Quick Start (Local)

### Prerequisites
* Python 3.10+
* A free [Groq API Key](https://console.groq.com/keys)

### 1. Clone the Repository
```bash
git clone [https://github.com/yourusername/agentic-news-analyst.git](https://github.com/yourusername/agentic-news-analyst.git)
cd agentic-news-analyst
2. Install Dependencies
Note: We pin specific versions to ensure compatibility between OpenAI and CrewAI.

Bash

pip install "openai==1.83.0" crewai==1.8.0 streamlit duckduckgo-search
3. Run the Application
Bash

streamlit run main.py
🐳 Run with Docker
This project is fully containerized for easy deployment.

1. Build the Image
Bash

docker build -t news-analyst .
2. Run the Container
Bash

docker run -p 8501:8501 news-analyst
Access the app at http://localhost:8501

🧩 Architecture Flow
Code snippet

graph TD
    A[User Input] --> B(Strategist Agent)
    B -->|Research Plan| C(Researcher Agent)
    C -->|Verified Facts| D(Writer Agent)
    D -->|Draft Report| E(Critic Agent)
    E -->|Polished Briefing| F[Final Output]
📸 Features
Transparent Logic: Click the "Expanders" in the UI to see the raw output of every agent (The Plan, The Data, The Draft).

Zero Cost: Uses Groq's free tier and Open Source tools.

Hallucination Check: The Critic agent specifically acts as a guardrail against false information.
