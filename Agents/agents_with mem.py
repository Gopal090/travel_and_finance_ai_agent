# agno is a framework to build ai agents
# pyrefly: ignore [missing-import]
import sys
from agno.agent import Agent  # type: ignore # pyrefly: ignore [missing-import]
from agno.models.groq import Groq  # type: ignore # pyrefly: ignore [missing-import]
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb
from agno.tools.duckduckgo import DuckDuckGoTools  # type: ignore # pyrefly: ignore [missing-import]

sys.stdout.reconfigure(encoding='utf-8')
load_dotenv()

db=SqliteDb(db_file="agno.db")
db.clear_memories()

def build_agent():
    return Agent(
        db=db,
        model=Groq(id="openai/gpt-oss-120b"), 
        markdown=True,
        add_datetime_to_context=True,
        add_history_to_context=True,
        
    )

agent = build_agent()

agent.print_response("what is transformer?")
agent.print_response("why is it so powerful?")


