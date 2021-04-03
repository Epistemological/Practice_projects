import string

alphabet = ' ' + string.ascii_lowercase
positions = {}
index = 0
for char in alphabet:
    positions[char] = index
    index += 1

message = "hi my name is caesar"
encoded_list = []
for char in message:
    position = positions[char]
    encoded_position = (position + 1) % 27
    encoded_list.append(alphabet[encoded_position])
    encoded_message = "".join(encoded_list)
print(encoded_message)

### Exercise 4
def encoding(message, key):
    encoded_list = []
    alphabet = ' ' + string.ascii_lowercase
    positions = {}
    index = 0
    for char in alphabet:
        positions[char] = index
        index += 1
    for char in message:
        position = positions[char]
        encoded_position = (position + key) % 27
        encoded_list.append(alphabet[encoded_position])
        encoded_message = "".join(encoded_list)
    return encoded_message
print(encoding(message, 3))

### Exercise 5

decoded_message = encoding(encoded_message, -1)
print(decoded_message)
