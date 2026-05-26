# from django.contrib import admin
# from django.urls import path, include
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

# urlpatterns = [
#     path('admin/', admin.site.urls),

#     path('api/', include('core.urls')),

#     # JWT AUTH
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/', TokenRefreshView.as_view(), name='token_refresh'),
# ]


# from django.db import models
# from django.contrib.auth.models import User


# class Wallet(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)

#     def __str__(self):
#         return f"{self.user.username}'s wallet"


# class Transaction(models.Model):
#     TRANSACTION_TYPES = (
#         ('deposit', 'Deposit'),
#         ('withdraw', 'Withdraw')
#     )

#     wallet = models.ForeignKey(
#         Wallet,
#         on_delete=models.CASCADE,
#         related_name='transactions'
#     )
#     transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
#     amount = models.DecimalField(max_digits=20, decimal_places=2)
#     time_stamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.transaction_type} - {self.amount}"
    

# from django.urls import path
# from .views import (
#     WalletListCreateAPI,
#     TransactionListAPI,
#     DepositAPI,
#     WithdrawAPI
# )

# urlpatterns = [
#     path("wallets/", WalletListCreateAPI.as_view()),
#     path("transactions/", TransactionListAPI.as_view()),
#     path("deposit/", DepositAPI.as_view()),
#     path("withdraw/", WithdrawAPI.as_view()),
# ]
# from django.contrib import admin
# from django.urls import path, include
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

# urlpatterns = [
#     path('admin/', admin.site.urls),

#     path('api/', include('core.urls')),

#   
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/', TokenRefreshView.as_view(), name='token_refresh'),
# ]


# from django.db import models
# from django.contrib.auth.models import User


# class Wallet(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)

#     def __str__(self):
#         return f"{self.user.username}'s wallet"


# class Transaction(models.Model):
#     TRANSACTION_TYPES = (
#         ('deposit', 'Deposit'),
#         ('withdraw', 'Withdraw')
#     )

#     wallet = models.ForeignKey(
#         Wallet,
#         on_delete=models.CASCADE,
#         related_name='transactions'
#     )
#     transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
#     amount = models.DecimalField(max_digits=20, decimal_places=2)
#     time_stamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.transaction_type} - {self.amount}"
    

# from django.urls import path
# from .views import (
#     WalletListCreateAPI,
#     TransactionListAPI,
#     DepositAPI,
#     WithdrawAPI
# )

# urlpatterns = [
#     path("wallets/", WalletListCreateAPI.as_view()),
#     path("transactions/", TransactionListAPI.as_view()),
#     path("deposit/", DepositAPI.as_view()),
#     path("withdraw/", WithdrawAPI.as_view()),
# ]