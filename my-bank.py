"""
Name: Shaarav Naik Steven Cromwell
Date: 4/29/2025
Purpose: To create a simple banking program that allows the user to create an account, deposit money, withdraw money, and check their balance.
"""
# my-bank.py
import pickle
import os
from BBankAccount import BankAccount, InvalidTransactionError
from BBSavingsAccount import SavingAccount

DATA_FILE = "accounts.dat"

# Load existing accounts if the file exists
def load_accounts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "rb") as f:
            return pickle.load(f)
    return {}

# Save all accounts at the end
def save_accounts(accounts):
    with open(DATA_FILE, "wb") as f:
        pickle.dump(accounts, f)

# Show the menu and get user choice
def main_menu():
    print("\n--- Welcome to My Bank ---")
    print("1. Open an account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Show balance")
    print("5. Show transactions")
    print("6. Get Interest Rate ")
    print("7. Exit")
    return input("Enter your choice: ")

# Get account by account number safely
def get_account(accounts):
    acc_number = input("Enter your account number: ")
    if acc_number not in accounts:
        print("Account number does not exist.")
        return None
    return accounts[acc_number]

def main():
    check_or_save = True
    accounts = load_accounts()
    while True:
        choice = main_menu()
        if choice == "1":
            name = input("Enter your name: ")
            acc_number = input("Enter a new account number: ")
            if acc_number in accounts:
                print("Account number already exists.")
                continue
            acc_type = input("Do you want a savings account or a checking account?").strip().lower()
            if acc_type == "savings":
                check_or_save = False
                
            elif acc_type == "checking":
                check_or_save = True
                
            else:
                raise InvalidTransactionError("That is not a valid account type")
            try:
                initial = float(input("Enter initial deposit: "))
                if check_or_save == False:
                    
                    try:
                        rate = float(input("Enter your interest rate in percent (between 1% and 25%)"))
                    except ValueError:
                        print("Invalid rate")
                    if rate > 25 or rate < 1:
                        raise InvalidTransactionError("Invalid rate, must be between 1% and 25%.")
                elif check_or_save == True:
                    print(" ")
                if initial < 0:
                    raise InvalidTransactionError("Initial deposit cannot be negative.")
                if check_or_save == True:
                    accounts[acc_number] = BankAccount(name, acc_number, initial)
                    
                elif check_or_save == False:
                    accounts[acc_number] = SavingAccount(name, acc_number, initial, rate)
                    
                print("Account created successfully.")
            except ValueError:
                print("Invalid amount.")
            except InvalidTransactionError as e:
                print(e)

        elif choice == "2":
            account = get_account(accounts)
            if account:
                try:
                    amount = float(input("Enter amount to deposit: "))
                    account.deposit(amount)
                    print("Deposit successful.")
                except (ValueError, InvalidTransactionError) as e:
                    print(e)

        elif choice == "3":
            account = get_account(accounts)
            if account:
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    account.withdraw(amount)
                    print("Withdrawal successful.")
                except (ValueError, InvalidTransactionError) as e:
                    print(e)

        elif choice == "4":
            account = get_account(accounts)
            if account:
                if type(account) == SavingAccount:
                    years = int(input("How may years has this account been open for? Max holding time is 100 years"))
                    if years > 100:
                        print("This value exceeds the maximum account holding time.)")
                    else:
                        result = account.showBalance(years)
                        print("{0:.2f}".format(result))
                else:
                    account.show_balance()

        elif choice == "5":
            account = get_account(accounts)
            if account:
                account.show_transactions()

        elif choice == "6":
            account = get_account(accounts)
            try:
                if account:
                    print(account.getInterestRate())
            except (AttributeError, InvalidTransactionError) as e:
                print(e)

        elif choice == "7":
            save_accounts(accounts)
            print("All data saved. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")



if __name__ == "__main__":
    main()
