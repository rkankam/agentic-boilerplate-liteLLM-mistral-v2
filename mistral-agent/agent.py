from google.adk.agents import Agent  
from google.adk.models.lite_llm import LiteLlm  
from google.adk.tools.mcp_tool import MCPToolset, StdioConnectionParams  
from mcp import StdioServerParameters  
import os  



toolset = MCPToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command='npx',
            args=['tavily-mcp@latest'],
            env={"TAVILY_API_KEY": os.environ.get("TAVILY_API_KEY")}
        ),
        timeout=10.0
    )
)
  
root_agent = Agent(  
    model=LiteLlm(  
        model="mistral/mistral-medium-latest",  # ← Paramètre model requis  
        api_key=os.environ.get("MISTRAL_API_KEY")  
    ),  
    name="mistral_agent",  
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge.',
    tools=[toolset]  
)
