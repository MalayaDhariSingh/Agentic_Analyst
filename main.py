import streamlit as st
from crewai import Agent, Task, Crew, Process
from crewai.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
import os
import time

# --- CONFIGURATION ---
st.set_page_config(page_title="Enterprise AI News Analyst", page_icon="🏢", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .stApp { background-color: #0E1117; color: white; }
    .stButton>button { background-color: #00AAFF; color: white; border-radius: 5px; }
    .agent-card { background-color: #262730; padding: 15px; border-radius: 10px; margin-bottom: 10px; border-left: 5px solid #00AAFF; }
    .step-card { background-color: #1E1E1E; padding: 10px; border-radius: 5px; margin-bottom: 5px; border-left: 3px solid #2ecc71; }
</style>
""", unsafe_allow_html=True)

st.title("🏢 Enterprise Agentic Analyst")
st.markdown("*Multi-Agent Workflow: Strategy -> Research -> Writing -> Quality Control*")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("⚙️ System Control")
    groq_api_key = st.text_input("Groq API Key", type="password", help="Get free key at console.groq.com")
    
    st.markdown("### 🤖 Active Agents")
    st.markdown("- **Strategist:** Plans the research angle")
    st.markdown("- **Researcher:** Scrapes the web")
    st.markdown("- **Writer:** Drafts the content")
    st.markdown("- **Critic:** Reviews and polishes")

# Main Input
col1, col2 = st.columns([3, 1])
with col1:
    topic = st.text_input("📝 Executive Briefing Topic:", placeholder="e.g., Impact of Quantum Computing on Banking")
with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    analyze_button = st.button("🚀 Launch Workflow", type="primary", use_container_width=True)

# Tool
@tool("DuckDuckGoSearch")
def search_tool(query: str):
    """Search the web for information."""
    return DuckDuckGoSearchRun().run(query)[:1000] 

if analyze_button:
    if not groq_api_key or not topic:
        st.error("❌ Missing Configuration!")
    else:
        try:
            # Setup Environment
            os.environ["OPENAI_API_KEY"] = groq_api_key
            os.environ["OPENAI_API_BASE"] = "https://api.groq.com/openai/v1"
            os.environ["OPENAI_MODEL_NAME"] = "llama-3.3-70b-versatile"
            
            # --- AGENTS ---
            strategist = Agent(
                role="Senior Strategist",
                goal=f"Plan the research angle for {topic}.",
                backstory="You are a veteran CTO.",
                verbose=True,
                allow_delegation=False
            )
            
            researcher = Agent(
                role="Deep Researcher",
                goal="Find data to support the strategy.",
                backstory="You are an expert at digging up hard-to-find facts.",
                tools=[search_tool],
                verbose=True,
                allow_delegation=False
            )
            
            writer = Agent(
                role="Executive Communicator",
                goal="Draft a briefing based on research.",
                backstory="You write for C-level executives. Concise and punchy.",
                verbose=True,
                allow_delegation=False
            )
            
            critic = Agent(
                role="Review Board",
                goal="Critique the draft and force improvements.",
                backstory="You are a harsh editor.",
                verbose=True,
                allow_delegation=False
            )

            # --- TASKS ---
            task1 = Task(
                description=f"Create a 3-bullet point research plan for {topic}. What are the key controversies?",
                agent=strategist,
                expected_output="A list of 3 research questions."
            )
            
            task2 = Task(
                description="Execute the research plan. Find 2-3 specific facts/numbers for each question.",
                agent=researcher,
                expected_output="A list of verified facts with sources."
            )
            
            task3 = Task(
                description="Write a draft briefing based on the facts.",
                agent=writer,
                expected_output="A 200-word draft."
            )
            
            task4 = Task(
                description="Review the draft. Fix grammar, remove 'I hope this helps', and make it sound professional.",
                agent=critic,
                expected_output="Final Polished Report."
            )

            crew = Crew(
                agents=[strategist, researcher, writer, critic],
                tasks=[task1, task2, task3, task4],
                process=Process.sequential,
                verbose=True,
                memory=False
            )

            # --- EXECUTION ---
            st.markdown("### 📡 Live Agent Feed")
            
            with st.status("🤖 Orchestrating Agents...", expanded=True) as status:
                st.write("🧠 **Strategist** is planning...")
                st.write("🕵️ **Researcher** is searching DuckDuckGo...")
                st.write("✍️ **Writer** is drafting...")
                st.write("⚖️ **Critic** is reviewing...")
                
                # Run the crew
                result = crew.kickoff()
                
                status.update(label="✅ Workflow Complete!", state="complete", expanded=False)

            # --- VISUALIZATION (THE PROOF) ---
            st.markdown("---")
            st.subheader("🔍 Transparent Agent Logic")
            
            with st.expander("1️⃣ View Strategist's Plan"):
                st.markdown(task1.output.raw)

            with st.expander("2️⃣ View Researcher's Data"):
                st.markdown(task2.output.raw)

            with st.expander("3️⃣ View Writer's Initial Draft"):
                st.markdown(task3.output.raw)
                
            with st.expander("4️⃣ View Critic's Final Polish"):
                st.markdown(task4.output.raw)

            # --- FINAL REPORT ---
            st.markdown("---")
            st.subheader("📄 Final Executive Report")
            st.markdown(f"""
            <div class="agent-card">
                {result}
            </div>
            """, unsafe_allow_html=True)
            
            st.download_button("📥 Download Report", str(result), "report.md")

        except Exception as e:
            st.error(f"Error: {str(e)}")