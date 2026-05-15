import json
import os

BASE_DIR = os.path.dirname(__file__)
FILE_PATH = os.path.join(BASE_DIR, "user.json")


def add_user(name, role):
    try:
        with open(FILE_PATH, "r") as file:
            users = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        users = []

    new_user = {"name": name, "role": role}
    users.append(new_user)

    with open(FILE_PATH, "w") as file:
        json.dump(users, file, indent=4)


def load_user():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def display_user():
    try:
        with open(FILE_PATH, "r") as file:
            datas = json.load(file)
            for data in datas:
                print(data)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No users found.")


def filter_search(role):
    try:
        with open(FILE_PATH, "r") as file:
            datas = json.load(file)

        found = False
        for data in datas:
            if data["role"] == role:
                print(data)
                found = True

        if not found:
            print("No users found for this role.")

    except (FileNotFoundError, json.JSONDecodeError):
        print("No users found.")


menu = """
===============
1. add user
2. load user
3. filter search
4. exit
===============
"""

print("WORKING DIR:", os.getcwd())

while True:
    print(menu)
    choice = input("enter your choice: ")

    if choice == "1":
        name = input("enter your name: ")
        role = input("enter your role: ")
        add_user(name, role)
        print("user added")

    elif choice == "2":
        print(load_user())

    elif choice == "3":
        role_choices = """
        1. admin
        2. user
        3. exit
        """
        print(role_choices)

        rolechoice = int(input("what role do you want to search for (1-3): "))

        if rolechoice == 1:
            filter_search("admin")
        elif rolechoice == 2:
            filter_search("user")
        elif rolechoice == 3:
            continue

    elif choice == "4":
        break