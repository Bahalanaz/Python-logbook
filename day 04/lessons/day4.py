# class Wallet:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance  

#     def get_balance(self):
#         return self.__balance

# class WalletService:
#     def __init__(self):
#         self.wallets = [] 

#     def create_wallet(self, wallet):
#         self.wallets.append(wallet)

# def deposit(balance, amount):
#     if amount <= 0:
#         return "Invalid amount"
#     balance += amount
#     return balance

# history = []
# history.append("Deposited 100")
# history.append("Withdrew 50")

# for h in history:
#     print(h)

# def cli():
#     while True:
#         print("\n1. Create\n2. Deposit\n3. Exit")
#         choice = input("Choose: ")

#         if choice == "3":
#             break

# class Wallet:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance

#     def get_balance(self):
#         return self.__balance

#     def deposit(self, amount):
#         if amount <= 0:
#             return "Invalid deposit"
#         self.__balance += amount
#         return self.__balance

# class WalletService:
#     def __init__(self):
#         self.wallets = {}  # key = owner name

#     def create_wallet(self, owner, balance):
#         if owner in self.wallets:
#             return "Wallet already exists"
#         self.wallets[owner] = Wallet(owner, balance)
#         return "Wallet created"

# class Wallet:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance
#         self.history = []

#     def deposit(self, amount):
#         if amount <= 0:
#             return "Invalid amount"
#         self.__balance += amount
#         self.history.append(f"Deposited {amount}")
#         return self.__balance

#     def withdraw(self, amount):
#         if amount > self.__balance:
#             return "Insufficient funds"
#         self.__balance -= amount
#         self.history.append(f"Withdrew {amount}")
#         return self.__balancefrom wallet_app.services.wallet_service import WalletService

# service = WalletService()

# while True:
#     print("\n=== WALLET APP ===")
#     print("1. Create Wallet")
#     print("2. Deposit")
#     print("3. Withdraw")
#     print("4. Check Balance")
#     print("5. View History")
#     print("6. Exit")

#     choice = input("Choose option: ")

#     if choice == "1":
#         owner = input("Enter owner name: ")
#         balance = float(input("Enter initial balance: "))
#         wallet = service.create_wallet(owner, balance)
#         print(f"Wallet created for {wallet.owner}")

#     elif choice == "2":
#         owner = input("Enter owner name: ")
#         amount = float(input("Enter amount: "))
#         print(service.deposit(owner, amount))

#     elif choice == "3":
#         owner = input("Enter owner name: ")
#         amount = float(input("Enter amount: "))
#         print(service.withdraw(owner, amount))

#     elif choice == "4":
#         owner = input("Enter owner name: ")
#         wallet = service.find_wallet(owner)

#         if wallet:
#             print(wallet.get_balance())
#         else:
#             print("Wallet not found")

#     elif choice == "5":
#         owner = input("Enter owner name: ")
#         history = service.get_history(owner)

#         if isinstance(history, str):
#             print(history)
#         else:
#             for h in history:
#                 print(h)

#     elif choice == "6":
#         break

#     else:
#         print("Invalid choice")