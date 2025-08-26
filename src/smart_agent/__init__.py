from dotenv import load_dotenv
import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

load_dotenv()

google_api_key = os.getenv("GEMINI_API_KEY")
print("DEBUG key:", google_api_key)
if not google_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

client = AsyncOpenAI(
    api_key=google_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=client,
)

# Agents export karo
psychologist_agent = Agent(
    name="Psychologist",
    instructions="You are an expert psychologist giving professional advice.",
    model=model,
)

gto_agent = Agent(
    name="GTO",
    instructions="You are a Group Testing Officer analyzing candidate behaviors.",
    model=model,
)

deputy_president_agent = Agent(
    name="Deputy President",
    instructions="You are Deputy President giving political analysis and guidance.",
    model=model,
)

# RunConfig export karo (agar zarurat ho)
config = RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True,
)

__all__ = [
    "psychologist_agent",
    "gto_agent",
    "deputy_president_agent",
    "config",
]
