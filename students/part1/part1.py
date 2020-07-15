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
    temp1 = round(temp)
    return f"{temp1}{DEGREE_SYBMOL}"

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
    temp_in_farenheit = round((temp_in_farenheit - 32) / (9/5))
    return f"{temp_in_farenheit:.2f}{DEGREE_SYBMOL}"

def calculate_mean(total, num_items):
    """Calculates the mean.
    
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers."""
    
    result = int(total) / int(num_items)
    return f"{(round(result))}"

def process_weather(forecast_file):

    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
# Day 1 
    All_days = []
    for days in forecast_file["DailyForecasts"][0:1]:
        Date_1 = convert_date(days["Date"])
        Mintemp_1 = convert_f_to_c(days["Temperature"]["Minimum"]["Value"]) 
        Maxtemp_1 = convert_f_to_c(days["Temperature"]["Maximum"]["Value"])
        Dayrainprob_1 = (days["Day"]["RainProbability"])
        Daylongphrase_1 = (days["Day"]["LongPhrase"])
        Nightrainprob_1 = (days["Night"]["RainProbability"])
        Nightlongphrase_1 = (days["Night"]["LongPhrase"])
        MintempF_1 = int(days["Temperature"]["Minimum"]["Value"])
        MaxtempF_1 = int(days["Temperature"]["Maximum"]["Value"])

# Day 2
    for days in forecast_file["DailyForecasts"][1:2]:
        Date_2 = convert_date(days["Date"])
        Mintemp_2 = convert_f_to_c(days["Temperature"]["Minimum"]["Value"]) 
        Maxtemp_2 = convert_f_to_c(days["Temperature"]["Maximum"]["Value"])
        Dayrainprob_2 = (days["Day"]["RainProbability"])
        Daylongphrase_2 = (days["Day"]["LongPhrase"])
        Nightrainprob_2 = (days["Night"]["RainProbability"])
        Nightlongphrase_2 = (days["Night"]["LongPhrase"])
        MintempF_2 = int(days["Temperature"]["Minimum"]["Value"])
        MaxtempF_2 = int(days["Temperature"]["Maximum"]["Value"])

# Day 3
    for days in forecast_file["DailyForecasts"][2:3]:
        Date_3 = convert_date(days["Date"])
        Mintemp_3 = convert_f_to_c(days["Temperature"]["Minimum"]["Value"]) 
        Maxtemp_3 = convert_f_to_c(days["Temperature"]["Maximum"]["Value"])
        Dayrainprob_3 = (days["Day"]["RainProbability"])
        Daylongphrase_3 = (days["Day"]["LongPhrase"])
        Nightrainprob_3 = (days["Night"]["RainProbability"])
        Nightlongphrase_3 = (days["Night"]["LongPhrase"])
        MintempF_3 = int(days["Temperature"]["Minimum"]["Value"])
        MaxtempF_3 = int(days["Temperature"]["Maximum"]["Value"])
        
# Day 4     
    for days in forecast_file["DailyForecasts"][3:4]:
        Date_4 = convert_date(days["Date"])
        Mintemp_4 = convert_f_to_c(days["Temperature"]["Minimum"]["Value"]) 
        Maxtemp_4 = convert_f_to_c(days["Temperature"]["Maximum"]["Value"])
        Dayrainprob_4 = (days["Day"]["RainProbability"])
        Daylongphrase_4 = (days["Day"]["LongPhrase"])
        Nightrainprob_4 = (days["Night"]["RainProbability"])
        Nightlongphrase_4 = (days["Night"]["LongPhrase"])
        MintempF_4 = int(days["Temperature"]["Minimum"]["Value"])
        MaxtempF_4 = int(days["Temperature"]["Maximum"]["Value"])

# Day 5
    for days in forecast_file["DailyForecasts"][4:5]:
        Date_5 = convert_date(days["Date"])
        Mintemp_5 = convert_f_to_c(days["Temperature"]["Minimum"]["Value"]) 
        Maxtemp_5 = convert_f_to_c(days["Temperature"]["Maximum"]["Value"])
        Dayrainprob_5 = (days["Day"]["RainProbability"])
        Daylongphrase_5 = (days["Day"]["LongPhrase"])
        Nightrainprob_5 = (days["Night"]["RainProbability"])
        Nightlongphrase_5 = (days["Night"]["LongPhrase"])
        MintempF_5 = int(days["Temperature"]["Minimum"]["Value"])
        MaxtempF_5 = int(days["Temperature"]["Maximum"]["Value"])

#5 Day Overview
    #Lowest Temp
        alldaysmin = []
        alldaysmin.append([Date_1, Mintemp_1])
        alldaysmin.append([Date_2, Mintemp_2])
        alldaysmin.append([Date_3, Mintemp_3])
        alldaysmin.append([Date_4, Mintemp_4])
        alldaysmin.append([Date_5, Mintemp_5])
        
    #Highest Temp
        alldaysmax = []
        alldaysmax.append([Maxtemp_1, Date_1])
        alldaysmax.append([Maxtemp_2, Date_2])
        alldaysmax.append([Maxtemp_3, Date_3])
        alldaysmax.append([Maxtemp_4,Date_4])
        alldaysmax.append([Maxtemp_5, Date_5])
        
    #avrerage low
        alldaysmin_F = []
        alldaysmin_F.append(MintempF_1)
        alldaysmin_F.append(MintempF_2)
        alldaysmin_F.append(MintempF_3)
        alldaysmin_F.append(MintempF_4)
        alldaysmin_F.append(MintempF_5)
        lownum_items = (len(alldaysmin_F))
        lowtotal = (sum(alldaysmin_F))
        low_avr = float(calculate_mean(lowtotal, lownum_items))
        
    #The average high 
        alldaysmax_F = []
        alldaysmax_F.append(MaxtempF_1)
        alldaysmax_F.append(MaxtempF_2)
        alldaysmax_F.append(MaxtempF_3)
        alldaysmax_F.append(MaxtempF_4)
        alldaysmax_F.append(MaxtempF_5)
        highnum_items = (len(alldaysmax_F))
        hightotal = (sum(alldaysmax_F))
        high_avr = float(calculate_mean(hightotal, highnum_items))
    #return function
        return f"5 Day Overview\n    The lowest temperature will be {(min(alldaysmin))[1]}, and will occur on {(min(alldaysmin))[0]}.\n    The highest temperature will be {(max(alldaysmax))[0]}, and will occur on {(max(alldaysmax))[1]}.\n    The average low this week is {(convert_f_to_c(low_avr))}.\n    The average high this week is {(convert_f_to_c(high_avr))}.\n\n\n------- {Date_1} -------\nMinimum Temperature: {Mintemp_1}\nMaximum Temperature: {Maxtemp_1}\nDaytime: {Daylongphrase_1}\n    Chance of rain: {Dayrainprob_1}\nNightime: {Nightlongphrase_1}\n    Chance of rain: {Nightrainprob_1}\n\n\n------- {Date_2} -------\nMinimum Temperature: {Mintemp_2}\nMaximum Temperature: {Maxtemp_2}\nDaytime: {Daylongphrase_2}\n    Chance of rain: {Dayrainprob_2}\nNightime: {Nightlongphrase_2}\n    Chance of rain: {Nightrainprob_2}\n\n\n------- {Date_3} -------\nMinimum Temperature: {Mintemp_3}\nMaximum Temperature: {Maxtemp_3}\nDaytime: {Daylongphrase_3}\n    Chance of rain: {Dayrainprob_3}\nNightime: {Nightlongphrase_3}\n    Chance of rain: {Nightrainprob_3}\n\n\n------- {Date_4} -------\nMinimum Temperature: {Mintemp_4}\nMaximum Temperature: {Maxtemp_4}\nDaytime: {Daylongphrase_4}\n    Chance of rain: {Dayrainprob_4}\nNightime: {Nightlongphrase_4}\n    Chance of rain: {Nightrainprob_4}\n\n\n------- {Date_5} -------\nMinimum Temperature: {Mintemp_5}\nMaximum Temperature: {Maxtemp_5}\nDaytime: {Daylongphrase_5}\n    Chance of rain: {Dayrainprob_5}\nNightime: {Nightlongphrase_5}\n    Chance of rain: {Nightrainprob_5}" 

if __name__ == "__main__":
    print(process_weather(forecast_file))
    print(type(forecast_file))

