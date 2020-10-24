def reverse_string(str2):
    rev_str = ""
    for i in range(len(str2)):
        rev_str += str2[len(str2) - (i + 1)]
    return rev_str

str1 = input()
rev_str1 = reverse_string(str1)

if str1 == rev_str1:
    print("Palindrome string")
else:
    print("non- palidrome string")