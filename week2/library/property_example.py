class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative.")

        self._balance = value


account = BankAccount(5000)

print(account.balance)

account.balance = 10000

print(account.balance)

account.balance = -500
