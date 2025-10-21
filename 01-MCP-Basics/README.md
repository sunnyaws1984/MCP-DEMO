Sample MCP Server Projects for DevOps & System Monitoring

This repository contains simple yet practical FastMCP demo projects that show how to build Model Context Protocol (MCP) servers for real-world DevOps scenarios — such as checking system metrics, Docker status, and exposing resources via MCP tools.

```
Check CPU usage and core count
Monitor memory utilization (used, free, total)
Verify if Docker is running on the host
Expose system metadata as a resource
Run as an HTTP MCP server (localhost or remote)

```
FastMCP is a lightweight Python framework for building MCP servers — systems that expose tools, data, and resources to LLMs or automation frameworks using the Model Context Protoco

```
# Create Virtual Env and  Clone the repo
python -m venv .venv
source .venv/Scripts/activate

git clone https://github.com/yourname/MCP-DEMO.git
cd MCP-DEMO/01-MCP-Basics

# Install dependencies
pip install fastmcp psutil
or 
pip install -r requirements.txt

```

# Tools to test MCP - MCP Inspector
```
npx @modelcontextprotocol/inspector
Install Node from here : https://nodejs.org/en/download
```