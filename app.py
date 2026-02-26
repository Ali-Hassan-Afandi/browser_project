import streamlit as st

st.title("My Automation System")

if st.button("Run Automation"):
    st.write("Running...")
    # call your automation function here
import asyncio
import os
from dotenv import load_dotenv
from browser_use import Agent, Browser, ChatBrowserUse

# Load variables from .env file
load_dotenv()

async def main():
    browser = Browser()
    agent = Agent(
        task="go to google.com search for the rotating (changig every 10 minutes) residential proxy monthly plan with the unlimited bandwidth and minimal cost. provide me the link. " \
        " " \
        "" \
        "",
        llm=ChatBrowserUse(),
        browser=browser,
    )
    history = await agent.run()
    print(history)

if __name__ == "__main__":
    asyncio.run(main())
