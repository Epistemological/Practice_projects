#mtd 1: using list comprehension

test_str = "GeeksforGeeks is best for Geeks"
test_sub = "Geeks"

print("Originalsträngen är: " + test_str)

print("Substrängen som ska hittas är: " + test_sub)

res = [i for i in range(len(test_str)) if test_str.startswith(test_sub, i)]

print("Startindex för substringarna är: " + str(res))

#mtd 2: using re.finditer()

import re

test_str = "GeeksforGeeks is best for Geeks"
test_sub = "Geeks"
print("The original string is: " + test_str)
print("The substring is " + test_sub)

res = [i.start() for i in re.finditer(test_sub, test_str)]
print("The start indices of the substrings are: " + str(res))

#