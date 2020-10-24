def reverse_string(str2):
    rev_str = ""
    for i in range(len(str2)):
        rev_str += str2[len(str2) - (i + 1)]
    return rev_str

num = int(input())

rev_num = reverse_string(str(num))

if num == int(rev_num):
    print("Palindrome string")
else:
    print("non- palidrome string")