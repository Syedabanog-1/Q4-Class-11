import os
import asyncio
import requests  # For Fetching API
import rich
from agents import Agent, ModelSettings, Runner, function_tool
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set. Please ensure it is defined in your .env file.")


# Define function tool correctly (only once)
@function_tool(
    name_override="Adding_Member_to_Whatsapp_group",
    description_override="Add a member to the whatsapp group only by the Admins"
)
def add_members() -> str:
    """
    This function returns the added member to the group 
    """
    members = []
    members.append("Ali")
    return f"Member {members} has been added to the group"


# Define Agent
whatsapp_agent = Agent(
    name="Whatsapp Agent",
    instructions="""You are an admin of a whatsapp group. 
    Your duty is to add members to the group.""",
    tools=[add_members]  # ✅ pass the function tool here
)


# Main runner
async def main():
    result = await Runner.run(
        whatsapp_agent,
        "Add a member to the whatsapp group",
    )

    rich.print(result.new_items)
    rich.print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
