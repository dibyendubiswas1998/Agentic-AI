from mcp.server.fastmcp import FastMCP
from typing import Union
import asyncio


# Wheather Server:
mcp = FastMCP("Wheather Server")


@mcp.tool()
async def wheather(city: str) -> str:
    """Get wheather information for a city."""
    return f"Weather in {city} is sunny."



if __name__ == "__main__":
    mcp.run(transport="streamable-http")