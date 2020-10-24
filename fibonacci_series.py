def fibonacci_series(n):
    if n <= 1:
        return n
    else :
        return fibonacci_series(n-1) + fibonacci_series(n-2)

num1 = int(input())

for i in range(num1):
    print(fibonacci_series(i))