# agno is a framework to build ai agents
# pyrefly: ignore [missing-import]
import sys
from agno.agent import Agent  # type: ignore # pyrefly: ignore [missing-import]
from agno.models.groq import Groq  # type: ignore # pyrefly: ignore [missing-import]
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools  # type: ignore # pyrefly: ignore [missing-import]
from agno.tools.yfinance import YFinanceTools  # type: ignore # pyrefly: ignore [missing-import]


sys.stdout.reconfigure(encoding='utf-8')
load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="openai/gpt-oss-120b"),
        tools=[YFinanceTools()], # websearch 
        markdown=True,
        description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
        instructions=["use given tools whenever possible. Format your response using markdown and use tables to display data where possible."],
        add_datetime_to_context=True,
        debug_mode=True
    )

agent = build_agent()

agent.print_response("Share the MSFT stock price in INR and analyst recommendations")

