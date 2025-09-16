# Sample Agent that orchestrates connections to built-in or custom MCP servers
# Currently using FoundryLocal for saving money 
# Change to any other SLM or LLM
import os
from langchain.agents import Tool, initialize_agent
from langchain.chat_models import ChatOpenAI
from foundry_local import FoundryLocalManager
from sample_mcp_client import greet


model_alias = "phi-3.5-mini"
manager = FoundryLocalManager(
    alias_or_model_id=model_alias,
    bootstrap=False
)

is_service_running = manager.is_service_running()
print(f"FoundryLocal service running: {manager.is_service_running()}")

if not is_service_running:
    print ("Starting FoundryLocal service...")
    manager.start_service()

print(f"Loading {model_alias} model...")
manager.load_model(model_alias)

# LangChain needs the following environment variables updated to use the FoundryLocal instead of actual OPENAI endpoint/API Key
os.environ["OPENAI_API_BASE"] = manager.endpoint
os.environ["OPENAI_API_KEY"] = manager.api_key # With FoundryLocal this is a dummy API Key

# LLM setup
llm = ChatOpenAI(
    model_name=manager.get_model_info(model_alias).id,
    temperature=0
)

# Configure tools available for the LLM
tools = [
    Tool(
        name="greeting",
        func=greet,
        description="Greet the given user"
    )
]

# Agent Setup
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=3,
)

# Sample orchestration of an Agent with just the "greeting" tool
if __name__ == "__main__":
    prompt = """
    1. STEP 1: Use the greeting tool with input "Bill". Do not display this output.
    2. STEP 2: Display a fortune cookie message that rhymes with the output of STEP 1.
    """
    result = agent.run(prompt)
    print("\n===== Agent Output =====\n", result)