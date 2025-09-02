import os
import asyncio
import rich
from agents import Agent, Runner, function_tool, trace
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set. Please ensure it is defined in your .env file.")


# Function Tool
@function_tool(name_override="Add_Number")
def Addition(num1: int = 600, num2: int = 400) -> int:
    """
    Args:
        num1 (int): First number
        num2 (int): Second number

    Returns:
        int : The sum of two numbers
    """
    return f"Sum of {num1} and {num2} is: {num1 + num2}"


addition_agent = Agent(
    name="Math Teacher",
    instructions="You are a helpful teacher. Use the tool to calculate sums.",
    tools=[Addition],
    
)

async def main():
    with trace("Addition"):
        result = await Runner.run(
            addition_agent,
            "Calculate sum of 50 and 25" 
        )
        rich.print(result)
        rich.print("\n[bold green]Final Answer:[/bold green]", result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
