import os
from agents import Agent, ModelSettings, Runner, function_tool,trace
import rich
#from connection import config
import asyncio
import requests # For Fetching API
from  dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set. Please ensure it is defined in your .env file.")



@function_tool(name_override="Get_Location", 
               description_override="Get the current location of a user")
def get_current_location() -> str:
    """ 
        Return the current location
    """
    # url = requests.get('my_google_maps_api')
    # return url.json()
    return "GH Sindh, Karachi"

current_location_assistant= Agent(
    name = "Agent",
    instructions=""" You are a helpful assistant always call a tool to get the location""",
    tools=[get_current_location]
)

async def main():
    with trace("Location Assistant"):
        result = await Runner.run(
            current_location_assistant,
            "Lead me the current location" 
        )
        rich.print(result)
        rich.print("\n[bold green]Final Answer:[/bold green]", result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
