# BankAccount.py
import datetime

class InvalidTransactionError(Exception):
    """Custom exception for invalid banking transactions."""
    pass

class BankAccount:
    def __init__(self, name, acc_number, initial_balance=0):
        self.name = name
        self.acc_number = acc_number
        self.balance = initial_balance
        self.transactions = []  # List of tuples: (timestamp, type, amount)

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidTransactionError("Deposit amount must be positive.")
        self.balance += amount
        self.transactions.append((datetime.datetime.now(), "Deposit", amount))

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidTransactionError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise InvalidTransactionError("Insufficient funds.")
        self.balance -= amount
        self.transactions.append((datetime.datetime.now(), "Withdraw", amount))

    def show_balance(self):
        print(f"Account holder: {self.name}")
        print(f"Current balance: ${self.balance:.2f}")

    def show_transactions(self):
        if not self.transactions:
            print("No transactions yet.")
            return
        print(f"Transaction history for {self.name}:")
        for t in self.transactions:
            timestamp, t_type, amount = t
            print(f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')} - {t_type} - ${amount:.2f}")
