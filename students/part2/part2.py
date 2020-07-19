import plotly.express as px
import pandas as pd
import json
from datetime import datetime

""""
A single time series graph that contains both the minimum and maximum temperatures for each day.
A single time series graph that contains the minimum, minimum “real feel”, and minimum “real feel
shade” temperatures."""


list = []
def jsondata (forecast_file):
    with open(forecast_file) as f:
        forecast_file = json.load(f)

    for day in forecast_file["DailyForecasts"]:
        min_temp = day["Temperature"]["Minimum"]["Value"] 
        max_temp = day["Temperature"]["Maximum"]["Value"]

        temps = {'min':min_temp, 'max': max_temp}
    #temps["Minimum Temperature"] = min_temp
    #temps["Maximum Temperarute"] = max_temp
        list.append (temps)
 
        
jsondata("data/forecast_5days_a.json")

print(list)

#df = pd.read_JSON("file name")

# Line Graphs
#fig = px.line(df, x="", y="", title="")
#fig.show()

#fig = px.line(
    #df, 
    #x=[""], 
    #y=[""], 
    #title=""
#)
#fig.show()

#line
#df_a = {
    #"our_data": [123, 132, 654, 345, 125, 498],
    #"more_data": [345, 67, 176, 245, 197, 391],
    #"columns": ["a", "b", "c", "d", "e", "f"]
#}
#fig = px.line(df_a, y="our_data", x="columns")
#fig.show()
