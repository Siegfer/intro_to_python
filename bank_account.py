class Phone:
    def __init__(self, phone_number):
        self.number = phone_number

    def call(self, other_number):
        print("Calling {} from {}.".format(self.number, other_number))

    def text(self, other_number, msg):
        print("Sending text from {} to {}:".format(self.number, other_number))
        print(msg)


class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.withdrawl = True
        self.interest_rate = 100*.02

    def deposit(self, amount):
        self.balance += amount

    def withdrawl(self, amount):
        self.balance -= amount
        if (self.balance < 0):
            self.withdrawl = False

    def accumulate_interest(self, amount):
        self.balance = self.balance+(self.interest_rate * amount)


class ChildrensAccount:
    def __init__(self, balance):
        super().__init__(balance):
        self.interest_rate = 0
