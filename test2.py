def add_time(start, duration, day = None):
    # --------------------------------------------------------------------------------------------------------------------------------------
    # COLLECT DATA

    # Parse start and duration
    start = start.split()
    meridiem = start[1]
    start = start[0].split(":")
    duration = duration.split(":")

    # Initialize weekdays and days
    weekdays_upp = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    days = 0

    

    # --------------------------------------------------------------------------------------------------------------------------------------
    # CALCULATE TIME PASSING
    
    # Sum hours and minutes
    hours = int(start[0]) + int(duration[0])
    minutes = int(start[1]) + int(duration[1])
        
    # If start was in PM, add 12 to hours
    if meridiem == "PM":
        hours += 12

    # If minutes >= 60, new_minutes = minutes % 60 AND hours += 1
    # minutes can never be more than 118 (i.e. 59+59) (therefore, <2h)
    if minutes >= 60:
        minutes = minutes % 60
        hours += 1
    
    # If hours >= 24, new_hours = hours % 24 AND days = hours / 24
    if hours >= 24:
        days = int(hours / 24)
        hours = hours % 24
    
        

    # --------------------------------------------------------------------------------------------------------------------------------------
    # CALCULATE NEW TIME
        
    # If hours > 12, PM and new_hours = hours - 12
    if hours > 12:
        meridiem = "PM"
        hours = hours - 12

    # If hours == 12, PM
    elif hours == 12:
        meridiem = "PM"
            
    # Else, AM
    else:
        if hours == 0:
            hours = 12
        meridiem = "AM"

        

    # --------------------------------------------------------------------------------------------------------------------------------------
    # FORMAT NEW TIME STRING

    # Format minutes
    if minutes < 10:
        minutes = f"0{minutes}"

    # Build string for new time
    new_time = f"{hours}:{minutes} {meridiem}"

    # If there is a day, += ", {weekday[i]}"
    if day != None:
        for i in weekdays:
            if i.upper() == day.upper():
                new_time += f", {weekdays[weekdays.index(i) + (days % 7) - len(weekdays)]}"
                break
        
    # If days == 1, += "(next day)" to string
    if days == 1:
        new_time += " (next day)"

    # If days > 1, += "([days] days later)" to string
    if days > 1:
        new_time += f" ({days} days later)"



    # --------------------------------------------------------------------------------------------------------------------------------------
    # RETURN VALUES

    # Return newly calculated time
    return new_time




print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("8:16 PM", "466:02", "tuesday"))
# Returns: 6:18 AM, Monday (20 days later)