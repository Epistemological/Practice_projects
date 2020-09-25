def find_the_longest_word(x):
    new_arr = x.split(' ')
    return (max(new_arr, key=len))

x = input("Input: ")

print(find_the_longest_word(x))