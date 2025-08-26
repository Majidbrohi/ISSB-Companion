import os
from dotenv import load_dotenv
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

# Load environment variables from .env file
load_dotenv()

# Load the API key from environment variables
google_api_key = os.getenv("GEMINI_API_KEY")
if not google_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

# Initialize the external client
external_client = AsyncOpenAI(
    api_key=google_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Define the model
model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client,
)

# Define the run configuration
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
)

# Define the GTO agent
gto_agent: Agent = Agent(
    name="Group Testing Officer",
    instructions=(
        "You are a Group Testing Officer (GTO) with expertise in assessing candidates' performance in group tasks and outdoor activities. "
        "Your role is to evaluate leadership qualities, teamwork, and decision-making skills. "
        "Provide feedback and assign scores based on their performance in group exercises and tasks."
    ),
    model=model,
)


