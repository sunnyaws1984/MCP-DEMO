from fastmcp import FastMCP
import psutil
import subprocess

# Create the MCP server
mcp = FastMCP(name="System Info MCP Server")

# ---------------------------
#  Tool 1: CPU Information
# ---------------------------
@mcp.tool
def cpu_info() -> dict:
    """Returns current CPU usage and core count."""
    return {
        "cpu_usage_percent": psutil.cpu_percent(interval=1),
        "cpu_core_count": psutil.cpu_count(logical=True),
    }

# ---------------------------
# Tool 2: Memory Information
# ---------------------------
@mcp.tool
def memory_info() -> dict:
    """Returns system memory usage details."""
    memory = psutil.virtual_memory()
    return {
        "total_gb": round(memory.total / (1024**3), 2),
        "used_gb": round(memory.used / (1024**3), 2),
        "free_gb": round(memory.available / (1024**3), 2),
        "usage_percent": memory.percent,
    }

# ---------------------------
#  Tool 3: Docker Status
# ---------------------------
@mcp.tool
def docker_status() -> str:
    """Checks if Docker daemon is running on this system."""
    try:
        subprocess.run(["docker", "info"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return " Docker is running and accessible."
    except Exception as e:
        return f"Docker is not running or not accessible: {e}"

# ---------------------------
# Resource (Static Info)
# ---------------------------
@mcp.resource("resource://system/info")
def system_metadata() -> dict:
    """Basic system metadata for identification."""
    return {
        "server_name": "FastMCP DevOps Node",
        "location": "Localhost",
        "maintainer": "Admin"
    }

# ---------------------------
# Run the server (HTTP mode)
# ---------------------------
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8080)
