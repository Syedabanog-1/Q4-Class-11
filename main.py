# import asyncio
from agents import Agent, Runner, function_tool, trace
from connection import config
import rich

@function_tool(
    name_override="Send_Email",
    description_override="Send an email to the user"
)
def send_email(from_email: str, to_email: str, subject: str, message: str) -> dict:
    """
    Args: 
        from_email (str): Email of the sender
        to_email (str): Email of the receiver
        subject (str): Subject of the email
        message (str): Body/content of the email

    Returns:
        dict: A dictionary containing the email details
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


async def main():
    with trace("class-11"):
      res= await Runner.run(
          email_agent,
          run_config=config
)
    print("Hello from q4-class-11!")
      

if __name__ == "__main__":
    main()
