import asyncio
from fastmcp import Client
import requests 
import json 
from dotenv import load_dotenv
import os
from openai import OpenAI

async def call_tool(tool_name: str, inputs: dict):
    async with Client("http://127.0.0.1:8000/mcp") as client:
        result = await client.call_tool(tool_name, inputs)
    return result

async def get_tools():
    async with Client("http://127.0.0.1:8000/mcp") as client:
        result = await client.list_tools()
    return result

async def get_prompts():
    async with Client("http://127.0.0.1:8000/mcp") as client:
        result = await client.list_prompts()
    return result

async def get_resources():
    async with Client("http://127.0.0.1:8000/mcp") as client:
        result = await client.list_resources()
    return result

async def use_resource(uri: str):
    async with Client("http://127.0.0.1:8000/mcp") as client:
        resource = await client.read_resource(uri)
    return resource
agent_prompt = """
You are a helpful calculator agent that can perform basic arithmetic operations. You have access to the following tools:
1. add(a: int, b: int) -> int: Adds two numbers and returns the result.
2. subtract(a: int, b: int) -> int: Subtracts the second number from the first and returns the result.

Your task is to use these tools to answer user queries related to arithmetic calculations. Always choose the most appropriate tool for the task at hand.
When you receive a user query, analyze it to determine which tool to use, and the inputs for that tool.
If the query involves addition, use the add tool. If it involves subtraction, use the subtract tool.
When using a tool, format your response as follows:
tool: <tool_name>
inputs: <input1>, <input2>
This a user query: What is 15 plus 27? in this case you should respond with:
'{"tool": "add", "inputs": [15, 27]}'

Remember to only use the tools provided and format your responses correctly.
"""

def decide_tool(user_query: str, agent_prompt: str, client) -> str:
    """Decide which tool to use based on the user query and agent prompt."""
    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": agent_prompt},
            {"role": "user", "content": user_query}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    import json
    load_dotenv()
    client = OpenAI()
    agent_answer = decide_tool("What is 50 minus 50?", agent_prompt, client)
    print(f"Decided tool: {agent_answer}")
    agent_answer_json = json.loads(agent_answer)
    tool_name = agent_answer_json["tool"]
    inputs = agent_answer_json["inputs"]
    print(f"Tool name: {tool_name}, inputs: {inputs}")
    tool_result = asyncio.run(call_tool(tool_name, {"a": inputs[0], "b": inputs[1]}))
    print(f"Tool result: {tool_result}")
    print(f"The result is: {tool_result.data}")
   
    # print(resp.output_text)
    # tools = asyncio.run(get_tools())
    # for tool in tools:
    #     if tool.name == tool_name.split(":")[1].strip():
    #         print("Using tool:")
    #         print(tool.name)
    #         print(tool.description)
    #         print(tool.inputSchema)
    #         print("-----")

    # prompts = asyncio.run(get_prompts())
    # print("Prompts:")
    # for prompt in prompts:
    #     print(prompt)
    #     print("-----")

    # resources = asyncio.run(get_resources())
    # print("Resources:")
    # for resource in resources:
    #     print(resource.uri)
    #     resource_content = asyncio.run(use_resource(resource.uri))
    #     print(resource_content)
    #     print("RESOURCE TEXT:")
    #     print(resource_content[0].text)
    #     print("-----")
