# Sample MCP Server

from fastmcp import FastMCP

mcp = FastMCP("Sample MCP Server")


@mcp.tool
def greet(name: str) -> str:
    """Greets an user."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    mcp.run()
