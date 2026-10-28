# agno is a framework to build ai agents
# pyrefly: ignore [missing-import]
from agno import agent
import sys
from agno.agent import Agent  # type: ignore # pyrefly: ignore [missing-import]
from agno.models.groq import Groq  # type: ignore # pyrefly: ignore [missing-import]
from agno.team import Team  
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools  # type: ignore # pyrefly: ignore [missing-import]

sys.stdout.reconfigure(encoding='utf-8')
load_dotenv()
eng_agent=Agent(name="English Agent", role="You answer questions in English")
chi_agent=Agent(name="Chinese Agent", role="You answer questions in Chinese")
hin_agent=Agent(name="Hindi Agent", role="You answer questions in Hindi")

# team_ leader pick the best agent to ans by default
team_leader=Team(
    name="Answer and translation Team",
    members=[eng_agent, chi_agent, hin_agent],
    model=Groq(id="qwen/qwen3.6-27b"),
    markdown=True,
    delegate_to_all_members=True,
    show_members_responses=True,
    instructions="Delegate the user's question to all member agents and include all three member responses (English, Chinese, and Hindi) in the final output."
)
    
team_leader.print_response("what is the capital of india?")

