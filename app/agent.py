"""
Your Legal Agent
"""

from langchain.agents import AgentExecutor
from langchain.agents import create_openai_functions_agent
from langchain.agents import load_tools
from langchain.tools import DuckDuckGoSearchRun
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder

from .llm import llm
from .memory import initialize_memory
from .memory import persist_memory
from .tools import get_word_length
from .tools import parse_web_search_results

AGENT_PURPOSE = """
    You are an assistant that only responds to questions about compliance for startups in California.
    Do not ask for permission to proceed.
    Always send information about regulations that is useful to the one asking questions.
    Try to keep the conversation flowing, consulting previous messages often.
    If you do web searches, parse the output so that the response is human-readable.
"""

tools = load_tools(
    [
        "llm-math",  # Let the LLM do math.
    ],
    llm=llm,
)
tools.append(get_word_length)  # Let the LLM count words accurately.
tools.append(DuckDuckGoSearchRun())  # Let the LLM do web searches.
tools.append(parse_web_search_results)  # Make sure web searches are parsed properly.

memory = initialize_memory()

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", AGENT_PURPOSE),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, memory=memory, verbose=True)


def ask(question: str) -> str:
    response = agent_executor.invoke({"input": question})
    persist_memory(agent_executor)
    return str(response['output'])
