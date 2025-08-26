from fastapi import FastAPI
from pydantic import BaseModel
from agents.run import Runner
from smart_agent.agents import psychologist_agent, gto_agent, deputy_president_agent

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/psychologist")
async def run_psychologist(req: PromptRequest):
    result = await Runner.run(psychologist_agent, req.prompt)
    return {"response": result.final_output}

@app.post("/gto")
async def run_gto(req: PromptRequest):
    result = await Runner.run(gto_agent, req.prompt)
    return {"response": result.final_output}

@app.post("/deputy-president")
async def run_deputy_president(req: PromptRequest):
    result = await Runner.run(deputy_president_agent, req.prompt)
    return {"response": result.final_output}
