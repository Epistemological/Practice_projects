test_list = []
print("Initial list: " + str(test_list))
alpha = 'a'
for i in range(0, 26):
    test_list.append(alpha)
    alpha = chr(ord(alpha) + 1)

print("List after insertion: " + str(test_list))