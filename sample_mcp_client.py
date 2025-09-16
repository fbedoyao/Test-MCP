# Sample MCP Client

import asyncio
from fastmcp import Client

# Connect to MCP server running on port 8000 (e.g. sample_mcp_server.py)
sample_client = Client("http://localhost:8000/mcp")

# Create other clients that connect to other MCP Servers as needed


# Use client to call Sample MCP Server to access "greet" tool from sample_mcp_server.py
def greet(name: str) -> str:
    async def _call():
        return await sample_client.call_tool("greet", {"name": name})

    return asyncio.run(_call())

# Call other MCP Servers' tools or resources