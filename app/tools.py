"""
Agent Tools
"""

from langchain.agents import tool
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

from .llm import llm


@tool
def get_word_length(word: str) -> int:
    """Returns the length of a word."""
    return len(word)


@tool
def parse_web_search_results(text: str) -> str:
    """Given a web search, this function uses an LLM to ensure the output is human-readable."""
    prompt_template = PromptTemplate.from_template(
        """
        The following text contains truncated information and ellipses (...)
        indicating incomplete sentences. Please rephrase it to be coherent and complete:
        \n\n
        {text}
        \n\n
        Rephrased text:
        """
    )
    response = llm.invoke(prompt_template.format(text=text), max_tokens=150)
    return StrOutputParser().invoke(response.content)
