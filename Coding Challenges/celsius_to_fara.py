celsius = int(input())

def conv(c):
    #your code goes here
    value = 9/5 * celsius + 32
    return value
    

fahrenheit = conv(celsius)
print(fahrenheit)