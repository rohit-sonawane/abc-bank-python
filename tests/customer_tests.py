from nose.tools import assert_equals, nottest, raises
from bank import Bank
from account import Account, CHECKING, SAVINGS
from customer import Customer


def test_statement():
    checkingAccount = Account(CHECKING)
    savingsAccount = Account(SAVINGS)
    henry = Customer("Henry").openAccount(checkingAccount).openAccount(savingsAccount)
    checkingAccount.deposit(100.0)
    savingsAccount.deposit(4000.0)
    savingsAccount.withdraw(200.0)
    assert_equals(henry.getStatement(),
                  "Statement for Henry" +
                  "\n\nChecking Account\n  deposit $100.00\nTotal $100.00" +
                  "\n\nSavings Account\n  deposit $4000.00\n  withdrawal $200.00\nTotal $3800.00" +
                  "\n\nTotal In All Accounts $3900.00")


def test_oneAccount():
    oscar = Customer("Oscar").openAccount(Account(SAVINGS))
    assert_equals(oscar.numAccs(), 1)


def test_twoAccounts():
    oscar = Customer("Oscar").openAccount(Account(SAVINGS))
    oscar.openAccount(Account(CHECKING))
    assert_equals(oscar.numAccs(), 2)


@nottest
def test_threeAccounts():
    oscar = Customer("Oscar").openAccount(Account(SAVINGS))
    oscar.openAccount(Account(CHECKING))
    assert_equals(oscar.numAccs(), 3)

bank = Bank()
checkingAccount = Account(CHECKING)
savingAccount = Account(SAVINGS)
bill = Customer("Bill")
bill.openAccount(checkingAccount)
bill.openAccount(savingAccount)
bank.addCustomer(bill)
checkingAccount.deposit(100.0)
checkingAccount.deposit(500.0)
checkingAccount.deposit(2000.0)
savingAccount.deposit(900.0)

from_acc = checkingAccount
to_acc = savingAccount

def test_transfer_success():
    transfer_amount = 100
    result = bill.transfer(from_acc, to_acc, transfer_amount)
    assert_equals(result, True)
    assert_equals(checkingAccount.sumTransactions(), 2500.0)
    assert_equals(savingAccount.sumTransactions(), 1000.0)

@raises(ValueError)
def test_transfer_insufficient_balance_failure():
    transfer_amount = 5000
    result = bill.transfer(from_acc, to_acc, transfer_amount)

@raises(ValueError)
def test_transfer_insufficient_balance_failure():
    checkingAccount_oscar = Account(CHECKING)
    oscar = Customer("Oscar").openAccount(checkingAccount_oscar)
    bank.addCustomer(oscar)
    checkingAccount_oscar.deposit(100.0)
    transfer_amount = 5000
    from_acc = checkingAccount_oscar
    to_acc = savingAccount
    result = bill.transfer(from_acc, to_acc, transfer_amount)

