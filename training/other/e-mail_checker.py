import re

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

def check(email):
    if(re.search(regex, email)):
        print("Valid Email")
    else:
        print("Invalid Email")

if __name__ == '__main__' :
    email = input("Put in the email address here: ")
    check(email)
