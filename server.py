from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    """
    Greets a user by their name. Use this tool when you need to provide a personalized greeting.

    Args:
        name (str): The first name of the person to greet.
    """
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)