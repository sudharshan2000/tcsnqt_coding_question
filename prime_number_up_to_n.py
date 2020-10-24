def prime(num):
    if num == 2:
        return True
    else:
        i = 2
        f = 0
        while(i < num/2):
            if num % i == 0:
                f = 0
                break
            else:
                f = 1
            i += 1
    if f == 0:
        return False
    else:
        return True

n = int(input())
prime_ls = []
for i in range(1,n+1):
    if prime(i) == True:
        prime_ls.append(i)
print(prime_ls)
