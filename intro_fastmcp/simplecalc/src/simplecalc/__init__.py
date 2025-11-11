from fastmcp import FastMCP
from fastmcp.prompts.prompt import Message, PromptMessage, TextContent
from fastmcp.resources import FileResource, TextResource, DirectoryResource
mcp = FastMCP("simplecalc")


@mcp.tool
def add(a: int, b:int) -> int:
    """Add two numbers."""
    return a + b

@mcp.tool
def subtract(a: int, b: int) -> int:
    """Subtract two numbers."""
    return a - b


def main() -> None:
    # mcp.add_resource(notice_resource)
    mcp.run(transport="http")
