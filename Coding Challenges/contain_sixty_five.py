def contain_sixty_five(num1,num2):
    num3 = num1 + num2
    if ((num1 == 65 or num2 == 65) or str(65) in str(num3)):
        return True
    return False


print(contain_sixty_five(63,2))
print(contain_sixty_five(65, 0))
print(contain_sixty_five(1, 2))
print(contain_sixty_five(65, 65))