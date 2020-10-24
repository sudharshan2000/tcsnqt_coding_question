def gcd_2_num(n,m):
    if m == 0:
        return n
    return gcd_2_num(m , n % m)

num1 = int(input())
num2 = int(input())
print(gcd_2_num(num1,num2))