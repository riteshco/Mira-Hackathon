from mira_sdk import MiraClient, CompoundFlow
from mira_sdk.exceptions import FlowError
import os

# client = MiraClient(config={"API_KEY": os.getenv("MIRA_API_KEY")})
client = MiraClient(config={"API_KEY": "sb-a17e177d1136349f0199d7ef2afd7829"}) 
flow = CompoundFlow(source="./flow.yaml")           # Load flow configuration

try:
    client.flow.deploy(flow)                               # Deploy to platform
    print("Compound flow deployed successfully!")          # Success message
except FlowError as e:
    print(f"Deployment error: {str(e)}")                   # Handle deployment error
