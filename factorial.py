def factorial(n):
    if n == 0 or n == 1:
        return n
    return n * factorial(n - 1)

num1 = int(input())
fact = factorial(num1)
print(fact)