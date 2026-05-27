import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dotenv import load_dotenv

from langchain.agents import Tool
from langchain.agents import initialize_agent
from langchain.agents import AgentType

from langchain_openai import ChatOpenAI

from tools.flight_tool import flight_search
from tools.hotel_tool import hotel_search
from tools.places_tool import places_search
from tools.weather_tool import weather_tool


# =========================================================
# LOAD API KEY
# =========================================================

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# =========================================================
# LLM
# =========================================================

llm = ChatOpenAI(
    temperature=0.3,
    model="gpt-3.5-turbo",
    api_key=OPENAI_API_KEY
)


# =========================================================
# TOOLS
# =========================================================

tools = [

    Tool(
        name="Flight Search",
        func=flight_search,
        description="""
        Search flights using the flights dataset.

        Example:
        Hyderabad to Delhi on 2025-01-04
        """
    ),

    Tool(
        name="Hotel Search",
        func=hotel_search,
        description="""
        Search hotels using the hotels dataset.

        Example:
        budget hotel in Delhi with breakfast
        """
    ),

    Tool(
        name="Places Search",
        func=places_search,
        description="""
        Search tourist places using the places dataset.

        Example:
        lakes in Delhi
        temples in Delhi
        """
    ),

    Tool(
        name="Weather Search",
        func=weather_tool,
        description="""
        Get weather forecast for a city.

        Example:
        Delhi
        Goa
        Mumbai
        """
    )

]


# =========================================================
# PROMPT
# =========================================================

prefix = """
You are an AI Travel Planner.

You MUST ONLY use the provided datasets and tool outputs.

DO NOT make up any flights, hotels, or places.

You must provide:

1. Flight Details
2. Hotel Recommendation
3. Tourist Places
4. Weather Forecast
5. Estimated Budget

Always calculate budget.

Budget Formula:
Total Budget =
Flight Price +
(Hotel Price × Number of Days)

If number of days is not given,
assume 1 day.

Format output properly.
"""


# =========================================================
# AGENT
# =========================================================

agent_executor = initialize_agent(

    tools=tools,

    llm=llm,

    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,

    verbose=True,

    agent_kwargs={
        "prefix": prefix
    }

)


# =========================================================
# FUNCTION FOR STREAMLIT
# =========================================================

def generate_travel_plan(user_input):

    response = agent_executor.invoke({
        "input": user_input
    })

    return response["output"]


# =========================================================
# TERMINAL TESTING
# =========================================================

if __name__ == "__main__":

    print("\n=========== AI TRAVEL PLANNER ===========\n")

    user_input = input("Enter your travel request: ")

    result = generate_travel_plan(user_input)

    print("\n=========== FINAL TRAVEL PLAN ===========\n")

    print(result)

    print("\n=========================================\n")