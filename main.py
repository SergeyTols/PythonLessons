# Duck type - утиная типизация (прочитать)
# Шпоргалка по всем методам в пайтон
#

class BankAccount:
    def __init__(self, owner, balance=0):
        self._owner = owner
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f'Депозит пополнен на сумму {amount}')
        else:
            print(f'Нельзя внести отрицательную сумму на депозит')

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f'Снята сумма {amount}')
        else:
            print(f'Не достаточно средств')

client1 = BankAccount
client1.deposit(500)
client1.withdraw(600)
print('Остаток:', client1.get_balance())

