from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import tool
from datetime import datetime

@tool
def save_to_file_tool(content: str, filename: str = None) -> str:
    """Useful for when you need to save the research paper to a text file. 
    Input should be the content of the research paper as a string, and an optional filename."""
    if filename is None:
        filename = f"research_paper_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content) 
    return f"data successfully saved to {filename}"

search = DuckDuckGoSearchRun()
@tool
def search_tool(query: str) -> str:
    """search the web for relevant information to answer the user's query. Use this tool when you need to find information on the internet."""
    return search.run(query)

api_wrapper = WikipediaAPIWrapper(top_k_results=3, doc_content_chars_max=4000)
@tool
def wikipedia_tool(query: str) -> str:
    """useful for when you need to answer questions about people, places, or things."""
    return api_wrapper.run(query)