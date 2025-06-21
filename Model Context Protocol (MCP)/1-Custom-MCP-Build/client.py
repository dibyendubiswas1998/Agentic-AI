from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from llm import AzureOpenAIHandler
import asyncio



# Create MCPC Client Using Multile Servers:

async def main():
    try:
        client = MultiServerMCPClient(
            {
                "math": {
                    "command": "python",
                    "args": ["math_server.py"],
                    "transport": "stdio",
                },
                "weather": {
                    "url": "http://localhost:8000/mcp",
                    "transport": "streamable_http",
                }
            }
        )
        
        llm = AzureOpenAIHandler().get_llm()
        
        try:
            tools = await client.get_tools()
            print("Successfully loaded tools:", [t.name for t in tools])
        
        except Exception as e:
            print(f"Failed to load tools: {str(e)}")
            return

        agent = create_react_agent(model=llm, tools=tools)
        
        # Test each tool individually first
        try:
            math_response = await agent.ainvoke(
                {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
            )
            print("Math response:", math_response['messages'][-1].content)
            
        except Exception as e:
            print(f"Math tool failed: {str(e)}")

        try:
            weather_response = await agent.ainvoke(
                {"messages": [{"role": "user", "content": "what is the weather in California?"}]}
            )
            print("Weather response:", weather_response['messages'][-1].content)
            
        except Exception as e:
            print(f"Weather tool failed: {str(e)}")

    except Exception as e:
        print(f"Main execution failed: {str(e)}")


asyncio.run(main())