import datetime


class BankAccount:
    clients = []
    interest_rate = 0.05

    def __init__(self, name, dob, gender, balance=0):
        self.name = name
        self.date_of_birth = dob
        self.gender = gender
        self.balance = balance
        BankAccount.clients.append(self)

    def deposit(self, amount):
        self.balance += amount
        print('${} has been deposited'.format(amount))

    def withdraw(self, amount):
        self.balance -= amount
        print('${} has been withdrawn'.format(amount))

    @classmethod
    def set_interest_rate(cls, rate):
        cls.interest_rate = rate

    def __repr__(self):
        return 'Client({}, {}, {})'.format(self.name, self.date_of_birth, self.gender)

    def __str__(self):
        return 'Client {} is {}'.format(self.name, self.gender)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


client1 = BankAccount('Ana', '1997-01-01', 'Female', 2000)
client2 = BankAccount('Ann', '1997-01-07', 'Female', 3000)
client1.deposit(1000)
print(BankAccount.interest_rate)
client1.set_interest_rate(0.07)
print(client2.interest_rate)
print(BankAccount.interest_rate)
my_date = datetime.date(2022, 3, 18)
print(client2.is_workday(my_date))
