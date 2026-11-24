users = {}

def password_valid(password):
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    return True


def register():
    print("\n--- Registration ---")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users:
        print("Username already exists!")
        return

    if not password_valid(password):
        print("Password must have:")
        print("- At least 8 characters")
        print("- One uppercase letter")
        print("- One lowercase letter")
        print("- One number")
        return

    users[username] = password
    print("Registration successful!")


def login():
    print("\n--- Login ---")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("Login successful!")
        print("Welcome", username)

        # Session
        logged_in = True

        while logged_in:
            print("\n1. Logout")
            choice = input("Enter choice: ")

            if choice == "1":
                logged_in = False
                print("Logged out successfully!")

    else:
        print("Invalid username or password!")


while True:
    print("\n===== USER AUTHENTICATION =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Program ended.")
        break
    else:
        print("Invalid choice!")