import os
from agents import Agent, ModelSettings, Runner, function_tool
import rich
# from connection import config
import asyncio
import requests  # For Fetching API
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set. Please ensure it is defined in your .env file.")


def is_Admin(*args, admin_name: str = "Ali", **kwargs) -> bool:
    """
    Check if the given admin_name is the actual Admin.
    Accepts extra args/kwargs because the framework may pass them.
    """
    return admin_name 


@function_tool(
    name_override="Adding_Member_to_Whatsapp_group",
    description_override="Add a member to the whatsapp group only by the Admins",
    is_enabled=is_Admin
)
def add_members() -> str:
    """
    This function returns the added member to the group.
    """
    return "Member has been added to the group"


whatsapp_agent = Agent(
    name="Whatsapp Agent",
    instructions="""You are an admin of a whatsapp group. 
    Your duty is to add members to the group.""",
    tools=[add_members]
)


async def main():
     result = await Runner.run(
        whatsapp_agent,
        "Add a member to the whatsapp group",
        #run_config=config,
    )
   
     rich.print(result.new_items)
     rich.print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
