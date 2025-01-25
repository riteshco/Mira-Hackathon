from dotenv import load_dotenv
from mira_sdk import MiraClient
import os
from mira_sdk import MiraClient, CompoundFlow
from mira_sdk.exceptions import FlowError

load_dotenv()

client = MiraClient(config={"API_KEY": "sb-e57cc9b8c6b772b5f56b2b4bd74bdc94"})
flow = CompoundFlow(source="./flow.yaml")           # Load flow configuration

test_input = {                                              # Prepare test inputs
    "prime_input_1": "Adventuruous",
    "prime_input_2": "6 days",
    "prime_input_3": "Delhi, India",
    "prime_input_4": "$1200",
    "prime_input_5": "flight",
    "prime_input_6": """ {
        "title": "Robbery at Central Market",
        "description": "Two men robbed a shop in Central Market late last night.",
        "content": "The incident occurred at 10 PM when the market was about to close...",
        "publishedAt": "2025-01-15T22:00:00Z",
        "source": "Local Times"
    },
    {
        "title": "Violent Assault in Downtown",
        "description": "A person was hospitalized after being attacked in Downtown.",
        "content": "Witnesses reported seeing a fight escalate into a serious assault...",
        "publishedAt": "2025-01-14T18:00:00Z",
        "source": "City News"
    } """,
}

try:
    response = client.flow.test(flow, test_input)           # Test entire pipeline
    print("Test response:", response)
except FlowError as e:
    print("Test failed:", str(e))                           # Handle test failure
