
import os
import asyncio
import rich
from typing import Dict
from dotenv import load_dotenv
from agents import Agent, ModelSettings, Runner, function_tool

# Load environment variables
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set. Please ensure it is defined in your .env file.")


@function_tool(
    name_override="BookingAssistant",
    description_override="Book a cab and set charges",
    is_enabled=True
)
def book_a_cab(by: str, to: str, amount: int) -> dict:
    """
    Args:
        by (str): User's current location
        to (str): User's destination
        amount (int): The amount to be charged for the ride
    
    Returns:
        dict: A dictionary containing current location, destination, and amount
    """
    return {
        "By": by,
        "To": to,
        "Amount": amount
    }

# Create agent
cab_booking_agent = Agent(
    name="Booking Agent",
    instructions="""
    You are a helpful assistant. Always call the tool to book a cab.
    """,
    tools=[book_a_cab],
)


# Main async function
async def main():
    result = await Runner.run(
        cab_booking_agent,
        "Book me a cab from Karachi to Lahore with 5000"
    )

    rich.print(result.new_items)
    rich.print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
