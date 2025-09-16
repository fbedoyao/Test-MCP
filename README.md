1. Create and activate virtual environment.
2. Install requirements: pip install -r requirements.txt
2. Run MCP Server on port 8000: fastmcp run sample_server.py:mcp --transport http --port 8000
3. Update agent.py to use any language model. Currently defaults to phi-3.5-mini SLM running locally via FoudryLocal service
4. Update tools or connections to mcp servers as needed
5. Update orchestrating prompt as needed
3. Run Agent orchestrator: python sample_agent.py

Sample Flow:

User Prompt -> Agent -> Language Model -> MCP Client -> Custom MCP Server -> Language Model -> Output
