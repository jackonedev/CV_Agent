import chainlit as cl
from main import main as agent
from utils.log_funcs import log_action


@cl.on_chat_start
async def init():

    langgraph = agent()

    cl.user_session.set("langgraph", langgraph)
    log_action("Langgraph agent initialized")
    msg = cl.Message(
        """\
Hello! I am a chatbot who can help you with questions related to Agustín Stigliano personal CV.
Hope to be helpful!
"""
    )

    await msg.send()


@cl.on_message
async def main(message: cl.Message):
    log_action("-" * 20)
    log_action(f"Received User message: {message.content}")

    langgraph = cl.user_session.get("langgraph")

    # Set up the streaming callback
    cb = cl.AsyncLangchainCallbackHandler(stream_final_answer=True)
    cb.answer_reached = True
    config = {"callbacks": [cb]}

    result = await langgraph.ainvoke(
        {"question": message.content}, config=config
    )
    log_action(f"Langgraph agent final response: {result}")
    answer = result.get("answer", "Sorry, I don't have an answer for that.")

    msg = cl.Message(content=answer)
    await msg.send()
