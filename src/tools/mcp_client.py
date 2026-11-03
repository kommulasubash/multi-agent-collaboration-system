
import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():

    server_params = StdioServerParameters(
        command="python",
        args=["src/mcp_server/server.py"]
    )

    async with stdio_client(server_params) as (
        read_stream,
        write_stream
    ):

        async with ClientSession(
            read_stream,
            write_stream
        ) as session:

            # Initialize MCP connection
            await session.initialize()

            # Discover tools
            response = await session.list_tools()

            print("\n========== AVAILABLE MCP TOOLS ==========\n")

            for tool in response.tools:

                # Handle tuple-based or object-based results
                if isinstance(tool, tuple):
                    name = tool[0]
                    description = tool[1] if len(tool) > 1 else ""
                else:
                    name = getattr(tool, "name", "Unknown")
                    description = getattr(
                        tool, "description", ""
                    )

                print(f"Tool Name: {name}")
                print(f"Description: {description}")
                print("-" * 40)

            # Test the search_knowledge tool
            print("\n========== TESTING MCP TOOL ==========\n")

            result = await session.call_tool(
                "search_knowledge",
                arguments={"query": "MCP"}
            )

            for item in result.content:
                if hasattr(item, "text"):
                    print(item.text)

            # Test calculate_statistics tool
            print("\n========== TESTING STATISTICS TOOL ==========\n")

            result = await session.call_tool(
                "calculate_statistics",
                arguments={
                    "numbers": [10, 20, 30, 40, 50]
                }
            )

            for item in result.content:
                if hasattr(item, "text"):
                    print(item.text)


if __name__ == "__main__":
    asyncio.run(main())
