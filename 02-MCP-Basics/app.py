from fastapi import FastAPI
from fastmcp import FastMCP
from datetime import datetime
import click
import pytz
import uvicorn


mcp = FastMCP(name="Weather & AQI Server")

# --------------------------------------
# Tool 1: Current Weather + Date & Time
# --------------------------------------
@mcp.tool()
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
@mcp.tool()
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


app=mcp.http_app(transport="streamable-http",stateless_http=True)

@click.command()
@click.option('--host', default='0.0.0.0')
@click.option('--port', default=9090)
def main(host, port):
    uvicorn.run(app, host=host, port=port)

if __name__ == "__main__":
    main()