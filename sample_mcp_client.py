# Sample MCP Client

import asyncio
from fastmcp import Client

# Connect to MCP server running on port 8000 (e.g. sample_mcp_server.py)
sample_client = Client("http://localhost:8000/mcp")

# Greet user using sample_mcp_server greeting tool
def greet(name: str) -> str:
    async def _call():
        async with sample_client:
            return await sample_client.call_tool("greet", {"name": name})

    return asyncio.run(_call())