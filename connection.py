import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel
from agents import RunConfig

# Load .env
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# Google Gemini ko OpenAI adapter ke sath use karna
external_client = AsyncOpenAI(
    api_key="AIzaSyATvBaIdKZ0matSe0FA7Xwox6ey9oi8-VY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Gemini model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)

# Run config
config = RunConfig(
    model=model,
    model_provider=external_client,
)
