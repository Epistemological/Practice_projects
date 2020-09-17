import random

def password(length):
    pw =str()
    characters = "abcdefghijklmnopqrstuvwxyzåäö" + "123456789" + "!¤%&/("
    for i in range(length):
        pw = pw + random.choice(characters)
    return pw

print(password(5))



