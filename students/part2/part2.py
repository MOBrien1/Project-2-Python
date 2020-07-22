import plotly.express as px
import pandas as pd
import json
from datetime import datetime

""""
A single time series graph that contains both the minimum and maximum temperatures for each day.
A single time series graph that contains the minimum, minimum “real feel”, and minimum “real feel
shade” temperatures."""

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%A %d %B %Y')

def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius

    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
    temp_in_farenheit = (temp_in_farenheit - 32) / (9/5)
    tempf_to_c = int(temp_in_farenheit)
    return tempf_to_c 

templist = []

def jsondata (forecast_file):
    with open(forecast_file) as f:
        forecast_file = json.load(f)

    for day in forecast_file["DailyForecasts"]:
        date = convert_date(day["Date"])
        min_temp = convert_f_to_c(day["Temperature"]["Minimum"]["Value"])
        max_temp = convert_f_to_c(day["Temperature"]["Maximum"]["Value"])
        real_feel_c = convert_f_to_c(day["RealFeelTemperature"]["Minimum"]["Value"])
        real_feel_shade_c = convert_f_to_c(day["RealFeelTemperatureShade"]["Minimum"]["Value"])

        temps = {"Date": date, "Min": min_temp, "Max": max_temp, 'Minimum Real Feel': real_feel_c, 'Minimum Real Feel Shade': real_feel_shade_c}

        templist.append(temps)

jsondata("data/forecast_5days_a.json")

df = pd.DataFrame(templist)

fig1 = px.line(
    df,  
    x= "Date",
    y= ["Min", "Max"],
    title="Forecast Temperatures: Minimum & Maximum",
    labels={
    "date": "Date"}
)

fig1.update_layout(
    yaxis_title = "Temperature (Degree's Celsius)",
    legend_title = "Temperature",
)

fig1.update_traces(mode="lines+markers")
fig1.show()

fig2 = px.line(
    df,  
    x= "Date",
    y= ["Min", "Minimum Real Feel", "Minimum Real Feel Shade"],
    title="Forecast Temperatures: Minimum",
    labels={"date": "Date"}
)

fig2.update_layout(
    yaxis_title = "Temperature (C)",
    legend_title = "Temperature",
    legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
    ),
    template = "ggplot2"
    )

fig2.update_traces(mode="lines+markers")
fig2.show()