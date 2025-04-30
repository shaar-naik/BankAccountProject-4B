from BBankAccount import BankAccount, InvalidTransactionError


class SavingAccount(BankAccount):

    def __init__(self, name, accountNumber, initialBalance=0, interestRate=0):
        super().__init__(name, accountNumber, initialBalance)
        self.interestRate = interestRate

    def setInterestRate(self, interestRate):
        self.interestRate = interestRate

    def getInterestRate(self):
        return self.interestRate

    def showBalance(self, years):
        self.years = years
        months = years * 12
        interest = (self.interestRate / 100)/12 + 1
        for i in range(months):
            self.balance *= interest
        return self.balance

