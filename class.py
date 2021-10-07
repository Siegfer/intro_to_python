class BankAccount():
    def __init__(self, kind):
        self.kind = kind
        self.balance = 0
        self.overdraft_fees = 0

    def __str__(self):
        return f'This is a {self.kind} account'

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.amount -= amount
        if (self.amount < 0):
            self.overdraft_fees += 20
        return amount


nick_account = BankAccount('checking')
print(nick_account)
print(nick_account.balance)
