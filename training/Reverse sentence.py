def reversewords(input):
    inputwords = input.split(" ")
    inputwords = inputwords[-1::-1]
    output = ' '.join(inputwords)
    return output
if __name__ == "__main__":
    input = input("What do you want to reverse? ")
    print(reversewords(input))
