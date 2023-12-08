def time_converting(hour,minute,period):
    if period == "pm" and hour != 12:
        hour= hour + 12
    elif period == "am" and hour == 12:
        hour = 0
    return f"{hour:02d}{minute:02d}"

print (time_converting(8, 30, "pm"))

