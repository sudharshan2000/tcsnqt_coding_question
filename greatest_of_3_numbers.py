num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 > num2 and num1 > num3:
    print('num1 = ',num1," is greatest number")
elif num2 > num1 and num2 > num3:
    print('num2 = ',num2," is greatest number")
else:
    print('num3 = ',num3," is greatest number")