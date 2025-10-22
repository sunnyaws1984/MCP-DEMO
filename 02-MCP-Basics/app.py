from fastapi import FastAPI
from fastmcp import FastMCP
from datetime import datetime
import pytz
import uvicorn

app = FastAPI()
server = FastMCP(name="Weather & AQI Server")

# --------------------------------------
# Tool 1: Current Weather + Date & Time
# --------------------------------------
@server.tool()
def current_weather() -> dict:
    """
    Returns mock current weather and date/time for Pune.
    """
    now = datetime.now()
    return {
        "city": "Pune",
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "temperature_c": 25,
        "condition": "Partly Cloudy",
        "humidity_percent": 60,
        "wind_kmph": 10
    }

# --------------------------------------
# Tool 2: Air Quality Info (mock)
# --------------------------------------
@server.tool()
def air_quality() -> dict:
    """
    Returns mock air quality info for Pune.
    """
    return {
        "city": "Pune",
        "aqi": 85,               # Air Quality Index
        "category": "Moderate",  # AQI category
        "pm2_5": 35,             # micrograms/m3
        "pm10": 60               # micrograms/m3
    }

# --------------------------------------
# Mount FastMCP on FastAPI
# --------------------------------------
mcp_app = server.http_app() # converts your FastMCP server into an ASGI app
app.mount("/", mcp_app)  # embeds the MCP app under /mcp in your main FastAPI app

@app.get("/health")
def health():
    return {"message": "FastAPI + FastMCP Weather & AQI Server Running"}

@app.get("/status")
def status():
    """
    Returns a simple status summary of the MCP server.
    """
    return {
        "server": "FastMCP Weather & AQI Server",
        "tools_available": ["current_weather", "air_quality"],
        "uptime": "Server just started"  # simple placeholder, can be enhanced
    }

def main():
    # Runs the MCP as an ASGI app
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)

if __name__ == "__main__":
    main()