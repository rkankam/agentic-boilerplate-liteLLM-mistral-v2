from google.adk.agents import Agent  
from google.adk.models.lite_llm import LiteLlm  
from google.adk.tools.mcp_tool import MCPToolset, StdioConnectionParams  
from mcp import StdioServerParameters  
import os  
import requests



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
  
def getOHLCV(pair: str, timeframe: str):
    # Get OHLCV by Pair Address
    # You can the timeframe, you can chose between 1s, 1m, 5m, 15m, 30m, 1h, 4h, 1d, 1w, 1M
    # You can only get the last 10 OHLCV data points
    # Example: pair = "93tjgwff5Ac5ThyMi8C4WejVVQq4tuMeMuYW1LEYZ7bu"
    # The API is provided by Moralis
    url = "https://solana-gateway.moralis.io/token/mainnet/pairs/" + pair + "/ohlcv?timeframe=" + timeframe + "&currency=usd&fromDate=2024-11-25&toDate=2024-11-26&limit=10"
    headers = {
        "Accept": "application/json",
        "X-API-Key": os.environ.get("MORALIS_API_KEY")
    }
    response = requests.request("GET", url, headers=headers)
    return response.json()

root_agent = Agent(  
    model=LiteLlm(  
        model="mistral/mistral-medium-latest",  # ← Paramètre model requis  
        api_key=os.environ.get("MISTRAL_API_KEY")  
    ),  
    name="mistral_agent",  
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge.',
    tools=[toolset,getOHLCV]  
)
