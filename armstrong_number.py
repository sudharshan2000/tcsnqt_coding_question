def armstrong_number(n):
    l = len(str(n))
    num_str = str(n)
    sum = 0
    for i in num_str:
        sum += (int(i) ** l)
    print(sum)
    return sum

num1 = int(input())

arm_num = armstrong_number(num1)

if num1 == arm_num:
    print('number is an armstrong number')
else:
    print('number is not an armstrong number')