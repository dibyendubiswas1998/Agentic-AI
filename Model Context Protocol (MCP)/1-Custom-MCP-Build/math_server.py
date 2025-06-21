from mcp.server.fastmcp import FastMCP
from typing import Union
import asyncio


# Initialize the FastMCP server:
# # Mentinon name of mcp server
mcp = FastMCP("Math-Server")


@mcp.tool()
async def addition(a:Union[int, float], b:Union[int, float]) -> Union[int, float]:
    """Add two numbers."""
    return a + b



@mcp.tool()
async def subtraction(a:Union[int, float], b:Union[int, float]) -> Union[int, float]:
    """Subtract two numbers."""
    return a - b



@mcp.tool()
async def multiplication(a:Union[int, float], b:Union[int, float]) -> Union[int, float]:
    """Multiply two numbers."""
    return a * b



@mcp.tool()
async def division(a:Union[int, float], b:Union[int, float]) -> Union[int, float]:
    """Divide two numbers."""
    return a / b


if __name__ == "__main__":
    mcp.run(transport="stdio")