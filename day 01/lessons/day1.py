import json
# OOP
# class User:
#     def __init__(self,name,email):
#         self.name = name
#         self.email = email 
    
# def display_info(self):
#     print(f"name:{self.name}")
#     print(f"name:{self.name}")

# user1 = User("kith","kith@gmail.com")

#Variables====================================================
# name ="kith"
# age = 20
# country = "philipines"
# pythonknowledge = True
# GPA = 4.0

# print(type(name))
# print(type(age))
# print(type(country))
# print(type(pythonknowledge))
# print(type(GPA))

# if and else===========================================
# password = "example of password"
# if len(password) >= 8:
#     print("that is a strong password")
# else:
#     print("weak password")

# role = "admin"
# is_logged_in = True

# if role == "admin" and is_logged_in == True:
#     print("welcome to the admin dashboard")
# else:
#     print("access denied")

# Students = ["kith","kheanne","Khaycee"]
#FOR LOOP====================================
# for name in Students:
#     print(name)

# i = 0
# while i <= 10:
#     if i == 5:
#         i+= 1
#         continue
#     print (i)
#     i+= 1
#functions=====================================
# def greet():
#     print("greetings")

# greet()

# def times(a, b):
#     c = a *b
#     return c


# result = times(5,5)
# print(result)

# def is_even(number):
#     if number % 2 == 0:
#         return "number is even"
#     else:
#         return "not even"

# num1 = 4
# result_2 = is_even(num1)

# print(result_2)

#dictionary========================================
# users = ["kith", "railey", "maramag"]
# print(users[0])
# users.append("alex")
# print(users)
# users.remove("alex")
# for user in users:
#     print(user)

# student = {
#     "name" : "kith",
#     "age" : 20,
#     "country" : "philippines"
# }

# print(student["name"])
# print(student["age"])
# print(student["country"])

# student["email"] = "kith@gmail.com"
# for key,value in student.items():
#     print(key,value)

# students = ["kith", "Alex","Maria","John"]
# students.append("Sarah")
# students.remove("Alex")
# for student in students:
#     print(student)

# student = {
#     "name":"kith",
#     "age": 20,
#     "course": "software"
# }

# student["grade"] = "A"

# for key,value in student.items():
#     print(f"{key} : {value}")

# users = [
#     {"name":"kith","role":"admin"},
#     {"name":"railey","role":"user"},
#     {"name":"maramag","role":"user"}
# ]

# for user in users:
#     print(user["name"] + " is " + user["role"])

# for user in users:
#     if user["role"] == "user":
#         print (user["name"])

#File manipulation=======================================
# with open(r"text.txt","r") as file: # read file
#     content = file.read()
#     print(content)

# with open(r"text.txt","w") as file: # writing filee
#     file.write("hello")

# with open(r"text.txt","a") as file: #append file
#     file.write("\nNew line added")

# with open(r"text.txt","r") as file: # read file
#     for line in file:
#         print(line)

# with open(r"text.txt","w") as file:
#     file.write("kith")
#     file.write("\n20")
#     file.write("\nsheesh")

# with open(r"text.txt","a") as file:
#     file.write("\nlearning python file handling")

# with open(r"text.txt","r") as file:
#     for line in file:
#         print(line)

# with open(r"text.txt","a") as file:
#     file.write("\nName: Kith, Role: Admin")
#     file.write("\nName: Railey, Role: User")
#     file.write("\nName: Maramag, Role: User")

# with open(r"text.txt","r") as file:
#     for line in file:
#         print(line)
#File Json manipulation=======================================
# student = {
#     "name" : "kith",
#     "course" : "software engineer",
#     "progress" : "day 1",
#     "active"  : True
# }
# student = [
#     {"name" : "kith","roles" : "admin"},
#     {"name" : "alex","roles" : "user"},
#     {"name" : "Maria","roles" : "user"}
# ]
# with open(r"student.json","w") as file:
#     json.dump(student,file)

# with open(r"student.json","r") as file:
#     data = json.load(file)

# for user in data:
#     print(user["name"] + "is" + user["roles"])

