import asyncio 
from fastmcp import Client 

client = Client("http://127.0.0.1:8000/mcp")

async def call_tool(name: str) -> str:
    async with client:
        result = await client.call_tool("greet", {"name": name})
        print(result)

def main():
    asyncio.run(call_tool("GILSAMAS"))
    asyncio.run(call_tool("ANOTHER_NAME"))
