from fastmcp import FastMCP 

mcp = FastMCP("My MCP server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

def main() -> None:
    mcp.run(transport="http", port=8000)

