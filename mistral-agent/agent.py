from google.adk.agents import Agent  
from google.adk.models.lite_llm import LiteLlm  
import os  

  
def get_stock_price(symbol: str):  
    """Fetches the stock price for a given symbol."""  
    # This is a placeholder function. Replace with actual implementation.  
    return f"The stock price for {symbol} is $100."  # Example response

root_agent = Agent(  
    model=LiteLlm(  
        model="mistral/mistral-medium-latest",  # ← Paramètre model requis  
        api_key=os.environ.get("MISTRAL_API_KEY")  
    ),  
    name="mistral_agent",  
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge.',
    tools=[get_stock_price]  
)
