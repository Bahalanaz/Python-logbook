# class Wallet:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance
#         self.history = []

#     def deposit(self, amount):
#         if amount <= 0:
#             return "invalid amount"
#         self.__balance += amount
#         self.history.append(f"Deposited {amount}")
#         return f"Deposited {amount}"

#     def withdraw(self, amount):
#         if amount <= 0 or amount > self.__balance:
#             return "invalid amount"
#         self.__balance -= amount
#         self.history.append(f"Withdrew {amount}")
#         return f"Withdrew {amount}"

#     def get_balance(self):
#         return self.__balance

#     def view_history(self):
#         return self.history