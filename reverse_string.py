str1 = input()
rev_str = ""
for i in range(len(str1)):
    rev_str += str1[len(str1) - (i + 1)]
print(rev_str)