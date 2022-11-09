def time_converter(number):
    hours = (number % 1440) // 60
    minutes = (number % 1440) % 60

    if(hours > 1) and (minutes > 1):
        return str(hours) + " hours and " + str(minutes) + " minutes"
    elif (hours > 1) and (minutes <= 1):
        return str(hours) + " hours and " + str(minutes) + " minute"
    elif (hours <= 1) and (minutes > 1):
        return str(hours) + " hour and " + str(minutes) + " minutes"
    else:
        return str(hours) + " hour and " + str(minutes) +  " minute"




print(time_converter(60))
print(time_converter(71))
print(time_converter(133))
print(time_converter(1))
print(time_converter(150))
print(time_converter(2000))


