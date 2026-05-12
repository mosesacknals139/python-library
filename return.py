user_name = "Moses1397"
password = 1234
def login():
    if (username == user_name and pasword == password):
        return "login successful"
    else:
        return "invalid username or password"


print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

print("@@@@@@@@@@@@this simple login page@@@@@@@@@@@@")
while True:
    username = input("enter your username: ")
    pasword = input("enter your password: ")
    print(login())
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@thank you for using this login page@@@@@@@@@@@@")