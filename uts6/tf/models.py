from django.db import models

# Create your models here.

# Modul User
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

# Modul Account
class Account:
    def __init__(self, user, balance=0):
        self.user = user
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient balance'
        else:
            self.balance -= amount
            return self.balance

# Modul Transaction
class Transaction:
    def __init__(self, sender: Account, receiver: Account):
        self.sender = sender
        self.receiver = receiver

    def transfer(self, amount):
        if self.sender.withdraw(amount) != 'Insufficient balance':
            self.receiver.deposit(amount)
            return 'Transfer successful'
        else:
            return 'Transfer failed'
