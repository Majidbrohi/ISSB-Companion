from dotenv import load_dotenv
import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
load_dotenv()

 
google_api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key = google_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model  = OpenAIChatCompletionsModel(
    model= "gemini-2.5-flash",
    openai_client=client,
)

    
# Define the agent with correct spelling and model
smart_agent = Agent(
    name="Defense Analyst",
    instructions="You are an expert defense and military analyst with proven skills in this field. You are a retired general of the Pakistan Armed Forces.",
    model= model
)


# Define the main function
result = Runner.run_sync(smart_agent, "who is the Army Chief of Pakistan?") 
print(result.final_output)