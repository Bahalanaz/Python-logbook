# from wallet_app.models.wallet import Wallet

# class WalletService:
#     def __init__(self):
#         self.wallets = []

#     def create_wallet(self, owner, balance=0):
#         wallet = Wallet(owner, balance)
#         self.wallets.append(wallet)
#         return wallet

#     def find_wallet(self, owner):
#         for wallet in self.wallets:
#             if wallet.owner == owner:
#                 return wallet
#         return None

#     def deposit(self, owner, amount):
#         wallet = self.find_wallet(owner)
#         if not wallet:
#             return "Wallet not found"
#         return wallet.deposit(amount)

#     def withdraw(self, owner, amount):
#         wallet = self.find_wallet(owner)
#         if not wallet:
#             return "Wallet not found"
#         return wallet.withdraw(amount)

#     def get_history(self, owner):
#         wallet = self.find_wallet(owner)
#         if not wallet:
#             return "Wallet not found"
#         return wallet.view_history()