def time_converting(hour,minute,period):#how output is formatted
    if period == "pm" and hour != 12: #if time is not in 24hr system and its under pm period you should add 12 hours to achieve that. 
        hour= hour + 12
    elif period == "am" and hour == 12:#set hour to 0 if period is am
        hour = 0
    return f"{hour:02d}{minute:02d}"#it is a formatted string with 2 decimal places

print (time_converting(8, 30, "pm"))

