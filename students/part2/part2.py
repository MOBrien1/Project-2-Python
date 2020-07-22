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

        temps = {"Date": date, "Min": min_temp, "Max": max_temp}

        templist.append(temps)

        
jsondata("data/forecast_5days_a.json")

print(templist)

df = templist
import plotly.graph_objs as go

# Line Graphs
fig = px.line(
    df, 
    x=["Min"],
    y=["Date"], 
    title="Forecast Temperatures: Minimum & Maximum"
)
#fig.show()


#fig = px.line(
    #df, 
    #x=[""], 
    #y=[""], 
    #title=""
#)
#fig.show()

#line

