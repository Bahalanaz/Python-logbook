import json

def add_user(name, role):
    with open("user.json", "r") as file:
        users = json.load(file)

    new_user = {"name": name, "role": role}
    users.append(new_user)

    with open("user.json", "w") as file:
        json.dump(users, file)

def load_user():
    with open(r"user.json","r") as file:
        data = json.load(file)
        return data

def display_user():
    with open(r"user.json","r") as file:
        datas = json.load(file)
        for data in datas:
            print(data)

def filter_search(role):
    with open(r"user.json","r") as file:
        datas = json.load(file)
        for data in datas:
            if data["role"] == role:
                print(data)

menu = """
===============
1.add user
2.load user
3.filter search
4.exit
===============
"""


            
while True:
    print(menu)
    choice = input("enter your choice:")

    if choice == "1":
        name = input("enter your name: ")
        role = input("enter your role: ")
        add_user(name,role)
        print("user added")
        
    elif choice == "2":
        print(load_user())


    elif choice == "3":
        role_choices= """
            1.admin
            2.user
            3.exit
        """
        rolechoice = int(input("what roles do you want to search for (1-2): "))
        print (role_choices)
        if rolechoice == 1:
            role = "admin"
            filter_search(role)
        elif rolechoice == 2:
            role = "user"
            filter_search(role)
        elif rolechoice == 3:
            break

    elif choice == 4:
        break
        


