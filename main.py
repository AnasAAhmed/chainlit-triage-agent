
from dotenv import load_dotenv
from agents import Runner,ItemHelpers
from my_agents.agents import triage_agent
import chainlit as cl
from chainlit.input_widget import Select, Switch, Slider
import asyncio
import json
from openai.types.responses import ResponseTextDeltaEvent

@cl.on_chat_start
async def start():
    """Set up the chat session when a user connects."""
    # Initialize an empty chat history in the session.
    cl.user_session.set("chat_history", [])
 
    settings = await cl.ChatSettings(
        [
            Select(
                id="model",
                label="Gemini Model",
                values=["gemini/gemini-2.0-flash"],
                initial_index=0,
            ),
        #    Slider(
        #         id="temperature",
        #         label="Temperature",
        #         tooltip="Temperature",
        #         initial=0.7,
        #         min=0,
        #         max=1,
        #         step=0.1,
        #     ),
            Switch(
                id="stream",
                label="Stream Responses",
                initial=True,
            )
        ]
    ).send()

    await cl.Message(content="Welcome to the Anas Ahmed Gemini Assistant! How can I help you today?").send()


@cl.on_settings_update
async def setup_agent(settings):
    # Save settings in user session
    cl.user_session.set("settings", settings)
    print("Updated settings:", settings)


@cl.on_message
async def main(message: cl.Message):
    loader = cl.Message(content="Thinking...")
    await loader.send()

    history = cl.user_session.get("chat_history") or []
    history.append({"role": "user", "content": message.content})

    full_response = ""
    settings = cl.user_session.get("settings") or {}
    isStream = settings.get("stream", True)

    msg = cl.Message(content="")
    await msg.send()

    try:
        if isStream:
            res = Runner.run_streamed(
                starting_agent=triage_agent,
                input=message.content  
            )
            first_token = True
            async for event in res.stream_events():
                if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                        token = event.data.delta
                        full_response += token 
                        print(token)
                        if first_token:
                           await loader.remove()
                           first_token = False

                        await msg.stream_token(token)
        else:
            result = Runner.run_sync(
                starting_agent=triage_agent,
                input=message.content  
            )
            full_response = result.final_output
            msg.content = result.final_output
            await loader.remove() 
            
        await msg.update()

        # Save assistant response to chat history
        history.append({"role": "assistant", "content": full_response})
        cl.user_session.set("chat_history", history)

    except Exception as e:
        msg.content = f"Error: {str(e)}"
        await msg.update()
        print(f"Error: {str(e)}")


@cl.on_chat_end
async def on_chat_end():
    # Retrieve the full chat history at the end of the session
    history = cl.user_session.get("chat_history") or []
    # Save the chat history to a file (or persist it elsewhere)
    with open("chat_history.json", "w") as f:
        json.dump(history, f, indent=2)
    print("Chat history saved.")
@cl.on_chat_resume
async def on_chat_resume(thread):
    pass

