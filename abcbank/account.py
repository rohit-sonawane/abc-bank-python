from transaction import Transaction
from date_provider import DateProvider

CHECKING = 0
SAVINGS = 1
MAXI_SAVINGS = 2


class Account:
    def __init__(self, accountType):
        self.accountType = accountType
        self.transactions = []

    def deposit(self, amount):
        if (amount <= 0):
            raise ValueError("amount must be greater than zero")
        else:
            self.transactions.append(Transaction(amount))

    def withdraw(self, amount):
        if (amount <= 0):
            raise ValueError("amount must be greater than zero")
        else:
            if self.sumTransactions() >= amount:
                self.transactions.append(Transaction(-amount))
            else:
                raise ValueError("Not sufficient amount in the account to withdraw")

    def interestEarned(self):
        days_in_year = 365
        actual_amount = self.sumTransactions()
        amount = actual_amount
        if self.accountType == SAVINGS:
            for day in range((self.transactions[-1].transactionDate - self.transactions[0].transactionDate).days):
                if amount <= 1000:
                    amount += amount * 0.001/days_in_year
                else:
                    amount += 1 + (amount - 1000) * 0.002/days_in_year
        if self.accountType == MAXI_SAVINGS:
            for each_transaction in self.transactions:
                if (DateProvider.now() - each_transaction.transactionDate).days <= 10:
                    amount += amount * 0.001/days_in_year
                else:
                    amount += amount * 0.05/days_in_year
        else:
            for day in range((self.transactions[-1].transactionDate - self.transactions[0].transactionDate).days):
                amount += amount * 0.001/days_in_year
        return amount - actual_amount

    def sumTransactions(self, checkAllTransactions=True):
        return sum([t.amount for t in self.transactions])
