from config.agent_config import MODEL
from agents import Agent


agent =Agent(
    model=MODEL,
    name='Translator',
    instructions=f'you are translator/interpreter agent fro human languages, translate the given text to this urdu'
)

nextjs_assistant =Agent(
    model=MODEL,
    name='Nextjs Teacher',
    instructions=f'You are a nextjs assistant teacher you answer question related of nextjs of user'
)


triage_agent = Agent(
    model=MODEL,
    name="Triage Agent",
    handoffs=[nextjs_assistant, agent],
    handoff_description="Choose between two agents: a Translator (for human language translation) and a Next.js Teacher (for Next.js related questions).",
    instructions="Route the user request to the most suitable agent."
)