def check_even_or_odd(n):
    if n % 2 == 0:
        return 'Even Number'
    else:
        return 'Odd Number'

num1 = int(input())

print(check_even_or_odd(num1))