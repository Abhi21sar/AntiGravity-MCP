from mcp.server.fastmcp import FastMCP
import os
import sys

# Initialize FastMCP server with host="0.0.0.0" and port=8080 for SSE accessibility
mcp = FastMCP("Local FileManager", host="0.0.0.0", port=8080)

# Define sandbox directory
SANDBOX_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sandbox")
if not os.path.exists(SANDBOX_DIR):
    os.makedirs(SANDBOX_DIR)

@mcp.tool()
def local_file_manager(operation: str, filename: str, content: str = "") -> str:
    """
    Read and write files in a safe sandbox directory.
    
    Args:
        operation: The operation to perform ('read' or 'write').
        filename: The name of the file to manage.
        content: The content to write (only used for 'write' operation).
    """
    # Security: Ensure we stay within the sandbox
    abs_sandbox = os.path.abspath(SANDBOX_DIR)
    target_path = os.path.abspath(os.path.join(abs_sandbox, filename))

    if not target_path.startswith(abs_sandbox):
        return "Error: Path is outside the sandbox."

    try:
        if operation == "read":
            if not os.path.exists(target_path):
                return f"Error: File {filename} not found."
            with open(target_path, "r") as f:
                return f.read()
        elif operation == "write":
            with open(target_path, "w") as f:
                f.write(content)
            return f"Success: File {filename} written."
        else:
            return f"Error: Unknown operation '{operation}'. Use 'read' or 'write'."
    except Exception as e:
        return f"Error handling file {filename}: {str(e)}"

if __name__ == "__main__":
    # Check for --sse flag to determine transport
    if "--sse" in sys.argv:
        # FastMCP handles the SSE transport with uvicorn
        mcp.run(transport="sse")
    else:
        # Default to stdio for local tools (Antigravity, Claude, etc.)
        mcp.run(transport="stdio")
