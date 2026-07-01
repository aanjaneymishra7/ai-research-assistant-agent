from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
# Added save_to_file_tool to the import list below
from tools import search_tool, wikipedia_tool, save_to_file_tool 

load_dotenv()

class SearchAgentInput(BaseModel):
    Topic: str = Field(description="The topic of the research")
    Summary: str = Field(description="Summary of findings")
    Source: list[str] = Field(description="List of sources used")
    tools_used: list[str] = Field(description="List of tools used")

# Note: "claude-v1" is deprecated; consider updating to "claude-3-5-sonnet-20240620"
llm = ChatAnthropic(model="claude-opus", temperature=0.7)
Parser = PydanticOutputParser(pydantic_object=SearchAgentInput)

prompt = ChatPromptTemplate.from_messages([
    ("system", 
     """You are a helpful research assistant that helps generate research papers.
     Complete the user query and use necessary tools to generate a research paper.
     
     Your final response MUST be a valid JSON object matching this schema:
     {format_instructions}
     """),
    ("placeholder", "{chat_history}"),
    ("human", "{query}"),
    ("placeholder", "{agent_scratchpad}"),
]).partial(format_instructions=Parser.get_format_instructions())

tools = [search_tool, wikipedia_tool, save_to_file_tool]

# Removed custom output_parser here so tool calling doesn't break
agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt) 
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

query = "Research the history of space exploration and save the final structured report to a file."
raw_response = executor.invoke({"query": query})

# Parse the final output text string into your Pydantic object
try:
    structured_response = Parser.parse(raw_response.get("output"))
    print("\n--- Structured Response ---")
    print(structured_response)
    print(f"Topic: {structured_response.Topic}")
except Exception as e:
    print(f"Error parsing structured response: {e}")
    print(f"Raw Output was: {raw_response.get('output')}")