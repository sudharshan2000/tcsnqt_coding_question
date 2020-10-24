n = int(input())
sum = 0
for i in range(len(str(n))):
    a = n % 10
    sum += a
    n = int(n / 10)
print(sum)