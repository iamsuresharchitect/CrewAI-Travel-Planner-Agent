"""Week 4 Day 3 - CrewAI Travel Planner Agent (Anthropic Claude).

Usage:
    Put ANTHROPIC_API_KEY=your-key in a .env file next to this script
    (optional) MODEL=anthropic/claude-haiku-5-5 in the same .env file
    python travel_planner.py
"""
import os
import sys

from crewai import LLM, Agent, Crew, Task
from dotenv import load_dotenv

# Load ANTHROPIC_API_KEY (and optional MODEL) from the .env file.
# The key is never hard-coded, and .env is git-ignored, so pushing is safe.
load_dotenv()
if not os.getenv("ANTHROPIC_API_KEY"):
    sys.exit("ANTHROPIC_API_KEY is missing. Add it to your .env file, then run again.")

llm = LLM(model=os.getenv("MODEL", "anthropic/claude-haiku-5-5"))

city = input("Which city? ").strip()
if not city:
    sys.exit("Please enter a city name.")

planner = Agent(
    role="Local Travel Planner",
    goal=(
        "Suggest exactly 3 memorable places that give a first-time visitor "
        "a true feel of the city they are visiting."
    ),
    backstory=(
        "You are a well-travelled guide who has spent twenty years showing "
        "first-time visitors around cities across the world. You know the "
        "must-see landmarks as well as the local tips, such as the best time "
        "of day to go, and you write short, friendly, practical advice "
        "instead of long essays."
    ),
    llm=llm,
    verbose=True,
)

task = Task(
    description=(
        "A traveller is visiting {city} and has only one day. Pick exactly 3 "
        "places in {city} that they should not miss. Choose a good mix "
        "(for example history, culture and local life) and make sure every "
        "place really exists in {city}."
    ),
    expected_output=(
        "A numbered list of exactly 3 lines and nothing else (no intro, no "
        "conclusion). Each line follows this format:\n"
        "1. <Place name> - <one short sentence on what it is, plus one "
        "practical tip>"
    ),
    agent=planner,
)

crew = Crew(agents=[planner], tasks=[task])

result = crew.kickoff(inputs={"city": city})
print(result)