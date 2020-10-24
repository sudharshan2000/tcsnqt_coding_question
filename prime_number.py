def prime(num):
    if num == 2:
        return 'Prime Number'
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
        return 'Non - Prime Number'
    else:
        return 'Prime Number'

n = int(input())

print(prime(n))