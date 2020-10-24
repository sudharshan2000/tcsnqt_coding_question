num = int(input())
rev_str = ""
num1 = str(num)
for i in range(len(num1)):
    rev_str += num1[len(num1) - (i + 1)]
print(int(rev_str))