def stringSplosion(initial_string):
    resulting_string = ""
    for s in range(len(initial_string)):
        resulting_string = resulting_string + initial_string[:s+1]
    return resulting_string

initial_string = input("Input: ")
print(stringSplosion(initial_string))

