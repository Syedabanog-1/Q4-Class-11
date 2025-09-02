import asyncio
from agents import Agent, Runner, function_tool, trace
from connection import config
import rich

# Tool definition
@function_tool(
    name_override="Send_Email",
    description_override="Send an email to the user"
)
def send_email(from_email: str, to_email: str, subject: str, message: str) -> dict:
    """
    Args:
        from_email: (str) send email from sender
        to_email: (str) email to receiver
        subject: (str) main subject to email
        message: (str) matter to write

    Return: dict with email details
    """
    return {
        "from": from_email,
        "to": to_email,
        "subject": subject,
        "message": message,
    }

# Email agent
email_agent = Agent(
    name="Email_Agent",
    instructions="I can help you send emails using the Send_Email tool.",
    tools=[send_email]
)

# Main runner
async def main():
    with trace("Class-11"):
        res = await Runner.run(
            email_agent,
            "Send an email to ali@test.com from gulzar@test.com "
            "with subject 'Meeting' and message 'See you at 5 PM'",
            run_config=config
        )
    rich.print(res.final_output)

if __name__ == "__main__":
    asyncio.run(main())
