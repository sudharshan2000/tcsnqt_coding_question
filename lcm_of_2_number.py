def gcd_2_num(n,m):
    if m == 0:
        return n
    return gcd_2_num(m , n % m)

def lcm_2_num(n1,m1):
    return int((n1 * m1) / (gcd_2_num(n1,m1)))

num1 = int(input())
num2 = int(input())
print(lcm_2_num(num1,num2))