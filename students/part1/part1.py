import json
with open("data/forecast_5days_a.json") as f:
    forecast_file = json.load(f)

from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and 'degrees celcius.'
    """
    return f"{temp}{DEGREE_SYBMOL}"

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%A %d %B %Y')

    #print(d.strftime('%A %d %B %Y'))


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius

    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
    temp_in_farenheit = (temp_in_farenheit - 32) / (9/5)
    return f"{temp_in_farenheit:.2f}{DEGREE_SYBMOL}"

def calculate_mean(total, num_items):
    """Calculates the mean.
    
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers."""
    
    result = int(total) / int(num_items)
    return f"{result}"

def process_weather(forecast_file):

    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """


# 19/06/2020 
    day_1 = {}
    for days in forecast_file["DailyForecasts"][0:1]:
        Date_1 = convert_date(days["Date"])
        Mintemp = convert_f_to_c(days["Temperature"]["Minimum"]["Value"]) 
        Maxtemp = convert_f_to_c(days["Temperature"]["Maximum"]["Value"])
        Dayrainprob = (days["Day"]["RainProbability"])
        Daylongphrase = (days["Day"]["LongPhrase"])
        Nightrainprob = (days["Night"]["RainProbability"])
        Nightlongphrase = (days["Night"]["LongPhrase"])

        day_1["Date"] = Date_1
        day_1["Minimum Temperature"] = Mintemp
        day_1["Maximum Temperature"] = Maxtemp
        day_1["Daytime"] = Daylongphrase
        day_1["Chance of rain"] = Dayrainprob
        day_1["Nighttime"] = Nightlongphrase
        day_1["Night Chance of rain"] = Nightrainprob

# 20/06/2020
    day_2 = {}
    for days in forecast_file["DailyForecasts"][1:2]:
        Date_2 = convert_date(days["Date"])
        Mintemp = convert_f_to_c(days["Temperature"]["Minimum"]["Value"]) 
        Maxtemp = convert_f_to_c(days["Temperature"]["Maximum"]["Value"])
        Dayrainprob = (days["Day"]["RainProbability"])
        Daylongphrase = (days["Day"]["LongPhrase"])
        Nightrainprob = (days["Night"]["RainProbability"])
        Nightlongphrase = (days["Night"]["LongPhrase"])

        day_2["Date"] = Date_2
        day_2["Minimum Temperature"] = Mintemp
        day_2["Maximum Temperature"] = Maxtemp
        day_2["Daytime"] = Daylongphrase
        day_2["Chance of rain"] = Dayrainprob
        day_2["Nighttime"] = Nightlongphrase
        day_2["Night Chance of rain"] = Nightrainprob
    
# 21/06/2020
    day_3 = {}
    for days in forecast_file["DailyForecasts"][2:3]:
        Date_3 = convert_date(days["Date"])
        Mintemp = convert_f_to_c(days["Temperature"]["Minimum"]["Value"]) 
        Maxtemp = convert_f_to_c(days["Temperature"]["Maximum"]["Value"])
        Dayrainprob = (days["Day"]["RainProbability"])
        Daylongphrase = (days["Day"]["LongPhrase"])
        Nightrainprob = (days["Night"]["RainProbability"])
        Nightlongphrase = (days["Night"]["LongPhrase"])

        day_3["Date"] = Date_3
        day_3["Minimum Temperature"] = Mintemp
        day_3["Maximum Temperature"] = Maxtemp
        day_3["Daytime"] = Daylongphrase
        day_3["Chance of rain"] = Dayrainprob
        day_3["Nighttime"] = Nightlongphrase
        day_3["Night Chance of rain"] = Nightrainprob
        
# 22/06/2020
    day_4 = {}     
    for days in forecast_file["DailyForecasts"][3:4]:
        Date_4 = convert_date(days["Date"])
        Mintemp = convert_f_to_c(days["Temperature"]["Minimum"]["Value"]) 
        Maxtemp = convert_f_to_c(days["Temperature"]["Maximum"]["Value"])
        Dayrainprob = (days["Day"]["RainProbability"])
        Daylongphrase = (days["Day"]["LongPhrase"])
        Nightrainprob = (days["Night"]["RainProbability"])
        Nightlongphrase = (days["Night"]["LongPhrase"])

        day_4["Date"] = Date_4
        day_4["Minimum Temperature"] = Mintemp
        day_4["Maximum Temperature"] = Maxtemp
        day_4["Daytime"] = Daylongphrase
        day_4["Chance of rain"] = Dayrainprob
        day_4["Nighttime"] = Nightlongphrase
        day_4["Night Chance of rain"] = Nightrainprob

# 23/06/2020
    day_5 = {}
    for days in forecast_file["DailyForecasts"][4:5]:
        Date_5 = convert_date(days["Date"])
        Mintemp = convert_f_to_c(days["Temperature"]["Minimum"]["Value"]) 
        Maxtemp = convert_f_to_c(days["Temperature"]["Maximum"]["Value"])
        Dayrainprob = (days["Day"]["RainProbability"])
        Daylongphrase = (days["Day"]["LongPhrase"])
        Nightrainprob = (days["Night"]["RainProbability"])
        Nightlongphrase = (days["Night"]["LongPhrase"])

        day_5["Date"] = Date_5
        day_5["Minimum Temperature"] = Mintemp
        day_5["Maximum Temperature"] = Maxtemp
        day_5["Daytime"] = Daylongphrase
        day_5["Chance of rain"] = Dayrainprob
        day_5["Nighttime"] = Nightlongphrase
        day_5["Night Chance of rain"] = Nightrainprob

    #print(f" {day_1}\n{day_2}\n{day_3}\n{day_4}\n{day_5} ")
#5 Day Overview
    alldaysmin = []
    alldaysmin.append([Date_1, day_1["Minimum Temperature"]])
    alldaysmin.append([Date_2, day_2["Minimum Temperature"]])
    alldaysmin.append([Date_3, day_3["Minimum Temperature"]])
    alldaysmin.append([Date_4, day_4["Minimum Temperature"]])
    alldaysmin.append([Date_5, day_5["Minimum Temperature"]])
    print(f"The lowest temperature will be {(min(alldaysmin))[1]}, and will occur on {(min(alldaysmin))[0]}.")
    

    alldaysmax = []
    alldaysmax.append([day_1["Maximum Temperature"], Date_1])
    alldaysmax.append([day_2["Maximum Temperature"], Date_2])
    alldaysmax.append([day_3["Maximum Temperature"], Date_3])
    alldaysmax.append([day_4["Maximum Temperature"],Date_4])
    alldaysmax.append([day_5["Maximum Temperature"], Date_5])
    print(f"The highest temperature will be {(max(alldaysmax))[0]}, and will occur on {(max(alldaysmax))[1]}.")
        
        
    #print(f"The highest temperature will be {(max((alldaysmax)[0:5]))}, and will occur on {(max(alldaysmax))[0]}")
#The average low this week is 11.7°C.

#The average high this week is 20.1°C.


#if __name__ == "__main__":
    #print(process_weather("data/forecast_5days_a.json"))


process_weather(forecast_file)