def contain_three(number1, number2):
    number3 = number1 + number2
    if ((number1 == 3 or number2 == 3) and str(3) in str(number3)):
        return True
    return False

print(contain_three(3,10))
print(contain_three(60,3))
print(contain_three(3,3))