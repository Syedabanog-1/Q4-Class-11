import os
import asyncio
import rich
from agents import Agent, Runner, function_tool
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set. Please ensure it is defined in your .env file.")


admin_name ="Ali"
def is_Admin(*args,admin_name: str = "Ali",**kwargs) -> bool:
    """
    Check if the given admin_name is an actual Admin.
    Accepts extra args/kwargs because the framework may pass them.
    """
    return admin_name 

# --- Function Tool ---
@function_tool(
    name_override="Adding_Member_to_Whatsapp_group",
    description_override="Add a member to the WhatsApp group only by the Admins",
    is_enabled=is_Admin
)
def add_member(member_name: str, group_name: str) -> str:
    """
    Add a member to the WhatsApp group.
    """
    return f"{member_name} has been added to the WhatsApp group '{group_name}'"

# --- Agent ---
whatsapp_agent = Agent(
    name="Whatsapp Agent",
    instructions="""
    You are an admin of a WhatsApp group. 
    Your duty is to add members to the group if you are an authorized admin.
    """,
    tools=[add_member]
)

# --- Main Runner ---
async def main():
    result = await Runner.run(
        whatsapp_agent,
        f"Add member {admin_name} to the WhatsApp group Python Learner"
    )
    rich.print(result.new_items)
    rich.print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
