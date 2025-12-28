#  Sample MCP Server Projects for DevOps & System Monitoring

This repository contains simple yet practical **FastMCP demo projects** that show how to build **Model Context Protocol (MCP) servers** for real-world DevOps and system monitoring use cases.

---

##  Overview

These examples demonstrate how to:

-  Check CPU usage and core count  
-  Monitor memory utilization (used, free, total)  
-  Verify if Docker is running on the host  
-  Expose system metadata as a resource  
-  Run an MCP server over HTTP (localhost or remote)

**FastMCP** is a lightweight Python framework for building MCP servers — systems that expose tools, data, and resources to LLMs or automation frameworks using the **Model Context Protocol**.

---

## Getting Started

### 1 Create Virtual Environment & Clone the Repo
```bash
python -m venv .venv
source .venv/Scripts/activate   # (Windows)
# or
source .venv/bin/activate       # (Linux/Mac)

git clone https://github.com/yourname/MCP-DEMO.git
cd MCP-DEMO/01-MCP-Basics

pip install fastmcp psutil
# or
pip install -r requirements.txt
```

### 2 Run the Application
```bash
python app.py

```

### 3 Test the MCP Application
```bash
 npx @modelcontextprotocol/inspector
 Enter this URL:  http://localhost:8080/mcp
 
 https://nodejs.org/en/download - Download Node from here if Node is missing

```

### 4 Dockerie the MCP Application
```bash
docker build -t mcp-system .
docker run -d -p 8080:8080 --name mcp-sysinfo mcp-system
```