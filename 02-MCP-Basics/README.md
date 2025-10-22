# Weather & AQI Server with FastMCP and FastAPI

This project demonstrates a simple **FastAPI** application integrated with **FastMCP** to expose multiple tools (APIs) and serve them via a unified HTTP interface. It also includes a separate FastAPI endpoint for products.

---

## Features

* **MCP Tools**

  * `current_weather`: Returns mock current weather and date/time for Pune.
  * `air_quality`: Returns mock air quality data for Pune.
* **Additional API**

  * `/products`: Returns a list of sample products.
* **Integrated Server**

  * FastAPI app runs alongside FastMCP HTTP endpoints.
* **Command-line Options**

  * Specify host and port using CLI options.

---

## Installation

1. Clone the repository:

```bash
git clone <repo-url>
cd <repo-folder>
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate        # Windows
```

3. Install dependencies:

```bash
pip install fastapi uvicorn fastmcp click pytz
or 
pip install -r requirements.txt
```

---

## Usage

Run the server:

```bash
python app.py 
```

* FastAPI endpoints will be available at `http://<host>:<port>/`
* FastMCP tools will be mounted at below location and can be connected via MCP inspector:
  `http://<host>:<port>/mcp-server/mcp`
  eg : http://localhost:9090/mcp-server/mcp

### Example Requests

**Get Current Weather**

```
GET /mcp-server/tools/current_weather
```

**Get Air Quality**

```
GET /mcp-server/tools/air_quality
```

**Get Products**

```
GET /products
```

Response:

```json
[
  {"name": "Laptop"},
  {"name": "Mouse"}
]
```

---

## Project Structure

```
.
├── app.py           # Main FastAPI + FastMCP app
├── README.md        # Project documentation
└── requirements.txt # Optional: dependencies list
```

---

## CLI Options

| Option   | Default | Description               |
| -------- | ------- | ------------------------- |
| `--host` | 0.0.0.0 | Host IP for the server    |
| `--port` | 9090    | Port to run the server on |

---

## Notes

* This project uses **mock data** for weather and air quality. Replace with real APIs if needed.
* FastMCP allows defining **tools** (like microservices) that can be e
