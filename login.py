def register():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

 with open("user.txt", "a") as f:
    f.write(username "," password "\n")

print("Registration successful!")

def login():
      username = input("Enter Username: ")
    password = input("Enter Password: ")

 with open("user.txt", "r") as f:
    for line in f:
        u, p = line.strip().split(",")
        if u == username and p == password:
            print("Login successful")
            return 
 print("invalid username or password")

while True:
    print("1. Register")
    print("2. Login")

    choice = input("Enter choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
        break
    else:
        print("invalid choice")