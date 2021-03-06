import json
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and 'degrees celcius.'
    """
    temp1 = round(temp,1)
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
    temp_in_farenheit = (temp_in_farenheit - 32) / (9/5)
    temp_in_farenheit_rounded = round(temp_in_farenheit,1)
    tempf_to_c = float(temp_in_farenheit_rounded)
    return tempf_to_c

def calculate_mean(total, num_items):
    """Calculates the mean.
    
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers."""
    
    result = int(total) / int(num_items)
    result1 = round(result,1)
    return result1

def process_weather(forecast_file):

    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
    with open(forecast_file, encoding="utf8") as f:
        forecast_file = json.load(f)
    
    # Day 1 
    Alldays = []
    for days in forecast_file["DailyForecasts"][0:1]:
        Date_1 = convert_date(days["Date"])
        Mintemp_1 = format_temperature(convert_f_to_c(days["Temperature"]["Minimum"]["Value"])) 
        Maxtemp_1 = format_temperature(convert_f_to_c(days["Temperature"]["Maximum"]["Value"]))
        Dayrainprob_1 = (days["Day"]["RainProbability"])
        Daylongphrase_1 = (days["Day"]["LongPhrase"])
        Nightrainprob_1 = (days["Night"]["RainProbability"])
        Nightlongphrase_1 = (days["Night"]["LongPhrase"])
        MintempF_1 = int(days["Temperature"]["Minimum"]["Value"])
        MaxtempF_1 = int(days["Temperature"]["Maximum"]["Value"])
        Alldays.append(1)
    # Day 2
    for days in forecast_file["DailyForecasts"][1:2]:
        Date_2 = convert_date(days["Date"])
        Mintemp_2 = format_temperature(convert_f_to_c(days["Temperature"]["Minimum"]["Value"])) 
        Maxtemp_2 = format_temperature(convert_f_to_c(days["Temperature"]["Maximum"]["Value"]))
        Dayrainprob_2 = (days["Day"]["RainProbability"])
        Daylongphrase_2 = (days["Day"]["LongPhrase"])
        Nightrainprob_2 = (days["Night"]["RainProbability"])
        Nightlongphrase_2 = (days["Night"]["LongPhrase"])
        MintempF_2 = int(days["Temperature"]["Minimum"]["Value"])
        MaxtempF_2 = int(days["Temperature"]["Maximum"]["Value"])
        Alldays.append(1)
    # Day 3
    for days in forecast_file["DailyForecasts"][2:3]:
        Date_3 = convert_date(days["Date"])
        Mintemp_3 = format_temperature(convert_f_to_c(days["Temperature"]["Minimum"]["Value"])) 
        Maxtemp_3 = format_temperature(convert_f_to_c(days["Temperature"]["Maximum"]["Value"]))
        Dayrainprob_3 = (days["Day"]["RainProbability"])
        Daylongphrase_3 = (days["Day"]["LongPhrase"])
        Nightrainprob_3 = (days["Night"]["RainProbability"])
        Nightlongphrase_3 = (days["Night"]["LongPhrase"])
        MintempF_3 = int(days["Temperature"]["Minimum"]["Value"])
        MaxtempF_3 = int(days["Temperature"]["Maximum"]["Value"])
        Alldays.append(1)   
    # Day 4     
    for days in forecast_file["DailyForecasts"][3:4]:
        Date_4 = convert_date(days["Date"])
        Mintemp_4 = format_temperature(convert_f_to_c(days["Temperature"]["Minimum"]["Value"])) 
        Maxtemp_4 = format_temperature(convert_f_to_c(days["Temperature"]["Maximum"]["Value"]))
        Dayrainprob_4 = (days["Day"]["RainProbability"])
        Daylongphrase_4 = (days["Day"]["LongPhrase"])
        Nightrainprob_4 = (days["Night"]["RainProbability"])
        Nightlongphrase_4 = (days["Night"]["LongPhrase"])
        MintempF_4 = int(days["Temperature"]["Minimum"]["Value"])
        MaxtempF_4 = int(days["Temperature"]["Maximum"]["Value"])
        Alldays.append(1)
    # Day 5
    for days in forecast_file["DailyForecasts"][4:5]:
        Date_5 = convert_date(days["Date"])
        Mintemp_5 = format_temperature(convert_f_to_c(days["Temperature"]["Minimum"]["Value"])) 
        Maxtemp_5 = format_temperature(convert_f_to_c(days["Temperature"]["Maximum"]["Value"]))
        Dayrainprob_5 = (days["Day"]["RainProbability"])
        Daylongphrase_5 = (days["Day"]["LongPhrase"])
        Nightrainprob_5 = (days["Night"]["RainProbability"])
        Nightlongphrase_5 = (days["Night"]["LongPhrase"])
        MintempF_5 = int(days["Temperature"]["Minimum"]["Value"])
        MaxtempF_5 = int(days["Temperature"]["Maximum"]["Value"])
        Alldays.append(1)
    #Day 6
    for days in forecast_file["DailyForecasts"][5:6]:
        Date_6 = convert_date(days["Date"])
        Mintemp_6 = format_temperature(convert_f_to_c(days["Temperature"]["Minimum"]["Value"])) 
        Maxtemp_6 = format_temperature(convert_f_to_c(days["Temperature"]["Maximum"]["Value"]))
        Dayrainprob_6 = (days["Day"]["RainProbability"])
        Daylongphrase_6 = (days["Day"]["LongPhrase"])
        Nightrainprob_6 = (days["Night"]["RainProbability"])
        Nightlongphrase_6 = (days["Night"]["LongPhrase"])
        MintempF_6 = int(days["Temperature"]["Minimum"]["Value"])
        MaxtempF_6 = int(days["Temperature"]["Maximum"]["Value"])
        Alldays.append(1)
    # Day 7
    for days in forecast_file["DailyForecasts"][6:7]:
        Date_7 = convert_date(days["Date"])
        Mintemp_7 = format_temperature(convert_f_to_c(days["Temperature"]["Minimum"]["Value"])) 
        Maxtemp_7 = format_temperature(convert_f_to_c(days["Temperature"]["Maximum"]["Value"]))
        Dayrainprob_7 = (days["Day"]["RainProbability"])
        Daylongphrase_7 = (days["Day"]["LongPhrase"])
        Nightrainprob_7 = (days["Night"]["RainProbability"])
        Nightlongphrase_7 = (days["Night"]["LongPhrase"])
        MintempF_7 = int(days["Temperature"]["Minimum"]["Value"])
        MaxtempF_7 = int(days["Temperature"]["Maximum"]["Value"])
        Alldays.append(1)
    #Day 8
    for days in forecast_file["DailyForecasts"][7:8]:
        Date_8 = convert_date(days["Date"])
        Mintemp_8 = format_temperature(convert_f_to_c(days["Temperature"]["Minimum"]["Value"])) 
        Maxtemp_8 = format_temperature(convert_f_to_c(days["Temperature"]["Maximum"]["Value"]))
        Dayrainprob_8 = (days["Day"]["RainProbability"])
        Daylongphrase_8 = (days["Day"]["LongPhrase"])
        Nightrainprob_8 = (days["Night"]["RainProbability"])
        Nightlongphrase_8 = (days["Night"]["LongPhrase"])
        MintempF_8 = int(days["Temperature"]["Minimum"]["Value"])
        MaxtempF_8 = int(days["Temperature"]["Maximum"]["Value"])
        Alldays.append(1)

    #5 Day Overview
    if len(Alldays) < 6:
        alldaysmin = []
        alldaysmax = []
        alldaysmin_F = []
        alldaysmax_F = []
        alldaysmin.append([MintempF_1, Date_1])
        alldaysmin.append([MintempF_2, Date_2])
        alldaysmin.append([MintempF_3, Date_3])
        alldaysmin.append([MintempF_4, Date_4])
        alldaysmin.append([MintempF_5, Date_5])

        alldaysmax.append([MaxtempF_1, Date_1])
        alldaysmax.append([MaxtempF_2, Date_2])
        alldaysmax.append([MaxtempF_3, Date_3])
        alldaysmax.append([MaxtempF_4, Date_4])
        alldaysmax.append([MaxtempF_5, Date_5])

        alldaysmin_F.append(MintempF_1)
        alldaysmin_F.append(MintempF_2)
        alldaysmin_F.append(MintempF_3)
        alldaysmin_F.append(MintempF_4)
        alldaysmin_F.append(MintempF_5)

        alldaysmax_F.append(MaxtempF_1)
        alldaysmax_F.append(MaxtempF_2)
        alldaysmax_F.append(MaxtempF_3)
        alldaysmax_F.append(MaxtempF_4)
        alldaysmax_F.append(MaxtempF_5)

        lownum_items = int(len(alldaysmin_F))
        lowtotal = int(sum(alldaysmin_F))
        low_avr = float(calculate_mean(lowtotal, lownum_items))
        highnum_items = int(len(alldaysmax_F))
        hightotal = int(sum(alldaysmax_F))
        high_avr = float(calculate_mean(hightotal, highnum_items))
        lowest_temp = convert_f_to_c((min(alldaysmin))[0])
        lowest_temp_day = min(alldaysmin)[1]
        highest_temp = convert_f_to_c((max(alldaysmax))[0])
        highest_temp_day = max(alldaysmax)[1]
        return f"5 Day Overview\n    The lowest temperature will be {(format_temperature(lowest_temp))}, and will occur on {lowest_temp_day}.\n    The highest temperature will be {(format_temperature(highest_temp))}, and will occur on {highest_temp_day}.\n    The average low this week is {(format_temperature(convert_f_to_c(low_avr)))}.\n    The average high this week is {(format_temperature(convert_f_to_c(high_avr)))}.\n\n-------- {Date_1} --------\nMinimum Temperature: {Mintemp_1}\nMaximum Temperature: {Maxtemp_1}\nDaytime: {Daylongphrase_1}\n    Chance of rain:  {Dayrainprob_1}%\nNighttime: {Nightlongphrase_1}\n    Chance of rain:  {Nightrainprob_1}%\n\n-------- {Date_2} --------\nMinimum Temperature: {Mintemp_2}\nMaximum Temperature: {Maxtemp_2}\nDaytime: {Daylongphrase_2}\n    Chance of rain:  {Dayrainprob_2}%\nNighttime: {Nightlongphrase_2}\n    Chance of rain:  {Nightrainprob_2}%\n\n-------- {Date_3} --------\nMinimum Temperature: {Mintemp_3}\nMaximum Temperature: {Maxtemp_3}\nDaytime: {Daylongphrase_3}\n    Chance of rain:  {Dayrainprob_3}%\nNighttime: {Nightlongphrase_3}\n    Chance of rain:  {Nightrainprob_3}%\n\n-------- {Date_4} --------\nMinimum Temperature: {Mintemp_4}\nMaximum Temperature: {Maxtemp_4}\nDaytime: {Daylongphrase_4}\n    Chance of rain:  {Dayrainprob_4}%\nNighttime: {Nightlongphrase_4}\n    Chance of rain:  {Nightrainprob_4}%\n\n-------- {Date_5} --------\nMinimum Temperature: {Mintemp_5}\nMaximum Temperature: {Maxtemp_5}\nDaytime: {Daylongphrase_5}\n    Chance of rain:  {Dayrainprob_5}%\nNighttime: {Nightlongphrase_5}\n    Chance of rain:  {Nightrainprob_5}%\n" 
    else:
    #10 Day Overview
        extdays_min = []
        extdays_max = []
        extdaysmin_F = []
        extdaysmax_F = []

        extdays_min.append([MintempF_1, Date_1])
        extdays_min.append([MintempF_2, Date_2])
        extdays_min.append([MintempF_3, Date_3])
        extdays_min.append([MintempF_4, Date_4])
        extdays_min.append([MintempF_5, Date_5])
        extdays_min.append([MintempF_6, Date_6])
        extdays_min.append([MintempF_7, Date_7])
        extdays_min.append([MintempF_8, Date_8])
        
        extdays_max.append([MaxtempF_1, Date_1])
        extdays_max.append([MaxtempF_2, Date_2])
        extdays_max.append([MaxtempF_3, Date_3])
        extdays_max.append([MaxtempF_4, Date_4])
        extdays_max.append([MaxtempF_5, Date_5])
        extdays_max.append([MaxtempF_6, Date_6])
        extdays_max.append([MaxtempF_7, Date_6])
        extdays_max.append([MaxtempF_8, Date_8])
        
        extdaysmin_F.append(MintempF_1)
        extdaysmin_F.append(MintempF_2)
        extdaysmin_F.append(MintempF_3)
        extdaysmin_F.append(MintempF_4)
        extdaysmin_F.append(MintempF_5)
        extdaysmin_F.append(MintempF_6)
        extdaysmin_F.append(MintempF_7)
        extdaysmin_F.append(MintempF_8)
        
        extdaysmax_F.append(MaxtempF_1)
        extdaysmax_F.append(MaxtempF_2)
        extdaysmax_F.append(MaxtempF_3)
        extdaysmax_F.append(MaxtempF_4)
        extdaysmax_F.append(MaxtempF_5)
        extdaysmax_F.append(MaxtempF_6)
        extdaysmax_F.append(MaxtempF_7)
        extdaysmax_F.append(MaxtempF_8)

        lownum_items_2 = (len(extdaysmin_F))
        lowtotal_2 = (sum(extdaysmin_F))
        low_avr_2 = float(calculate_mean(lowtotal_2, lownum_items_2))
        highnum_items_2 = (len(extdaysmax_F))
        hightotal_2 = (sum(extdaysmax_F))
        high_avr_2 = float(calculate_mean(hightotal_2, highnum_items_2))
        ext_lowest_temp = convert_f_to_c((min(extdays_min))[0])
        ext_lowest_temp_day = min(extdays_min)[1]
        ext_highest_temp = convert_f_to_c((max(extdays_max))[0])
        ext_highest_temp_day = max(extdays_max)[1]

        return f"8 Day Overview\n    The lowest temperature will be {format_temperature(ext_lowest_temp)}, and will occur on {ext_lowest_temp_day}.\n    The highest temperature will be {(format_temperature(ext_highest_temp))}, and will occur on {ext_highest_temp_day}.\n    The average low this week is {format_temperature((convert_f_to_c(low_avr_2)))}.\n    The average high this week is {format_temperature((convert_f_to_c(high_avr_2)))}.\n\n-------- {Date_1} --------\nMinimum Temperature: {Mintemp_1}\nMaximum Temperature: {Maxtemp_1}\nDaytime: {Daylongphrase_1}\n    Chance of rain:  {Dayrainprob_1}%\nNighttime: {Nightlongphrase_1}\n    Chance of rain:  {Nightrainprob_1}%\n\n-------- {Date_2} --------\nMinimum Temperature: {Mintemp_2}\nMaximum Temperature: {Maxtemp_2}\nDaytime: {Daylongphrase_2}\n    Chance of rain:  {Dayrainprob_2}%\nNighttime: {Nightlongphrase_2}\n    Chance of rain:  {Nightrainprob_2}%\n\n-------- {Date_3} --------\nMinimum Temperature: {Mintemp_3}\nMaximum Temperature: {Maxtemp_3}\nDaytime: {Daylongphrase_3}\n    Chance of rain:  {Dayrainprob_3}%\nNighttime: {Nightlongphrase_3}\n    Chance of rain:  {Nightrainprob_3}%\n\n-------- {Date_4} --------\nMinimum Temperature: {Mintemp_4}\nMaximum Temperature: {Maxtemp_4}\nDaytime: {Daylongphrase_4}\n    Chance of rain:  {Dayrainprob_4}%\nNighttime: {Nightlongphrase_4}\n    Chance of rain:  {Nightrainprob_4}%\n\n-------- {Date_5} --------\nMinimum Temperature: {Mintemp_5}\nMaximum Temperature: {Maxtemp_5}\nDaytime: {Daylongphrase_5}\n    Chance of rain:  {Dayrainprob_5}%\nNighttime: {Nightlongphrase_5}\n    Chance of rain:  {Nightrainprob_5}%\n\n-------- {Date_6} --------\nMinimum Temperature: {Mintemp_6}\nMaximum Temperature: {Maxtemp_6}\nDaytime: {Daylongphrase_6}\n    Chance of rain:  {Dayrainprob_6}%\nNighttime: {Nightlongphrase_6}\n    Chance of rain:  {Nightrainprob_6}%\n\n-------- {Date_7} --------\nMinimum Temperature: {Mintemp_7}\nMaximum Temperature: {Maxtemp_7}\nDaytime: {Daylongphrase_7}\n    Chance of rain:  {Dayrainprob_7}%\nNighttime: {Nightlongphrase_7}\n    Chance of rain:  {Nightrainprob_7}%\n\n-------- {Date_8} --------\nMinimum Temperature: {Mintemp_8}\nMaximum Temperature: {Maxtemp_8}\nDaytime: {Daylongphrase_8}\n    Chance of rain:  {Dayrainprob_8}%\nNighttime: {Nightlongphrase_8}\n    Chance of rain:  {Nightrainprob_8}%\n"
       
if __name__ == "__main__":
    print(process_weather("data/forecast_10days.json"))
    


