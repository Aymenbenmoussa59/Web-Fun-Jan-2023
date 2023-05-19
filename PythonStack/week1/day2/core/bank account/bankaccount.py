class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.interest_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5

    def display_account_info(self):
        print("Balance: $" + str(self.balance))

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate

# Create two accounts
account1 = BankAccount()
account2 = BankAccount()

# Account 1 transactions
account1.deposit(100)
account1.deposit(50)
account1.deposit(75)
account1.withdraw(30)
account1.yield_interest()
account1.display_account_info()  # Balance: $204.95

# Account 2 transactions
account2.deposit(200)
account2.deposit(50)
account2.withdraw(20)
account2.withdraw(100)
account2.withdraw(30)
account2.yield_interest()
account2.display_account_info()  # Balance: $191.25