# agno is a framework to build ai agents
# pyrefly: ignore [missing-import]
import sys
from agno.agent import Agent  # type: ignore # pyrefly: ignore [missing-import]
from agno.models.groq import Groq  # type: ignore # pyrefly: ignore [missing-import]
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools  # type: ignore # pyrefly: ignore [missing-import]

sys.stdout.reconfigure(encoding='utf-8')
load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="openai/gpt-oss-120b"),
        tools=[DuckDuckGoTools()], # websearch 
        markdown=True,
        instructions="You are a helpful and expert travel agent.",
        add_datetime_to_context=True
    )

agent = build_agent()

agent.print_response("is it safe to travel to pakistan today?")

