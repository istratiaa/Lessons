class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return self.__balance
        else:
            raise ValueError("Нельзя добавить отрицательную сумму")

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return self.__balance
        else:
            raise ValueError("баланс меньше суммы списания")

    # @property
    # def balance(self):
    #     return self.__balance
    #
    # @balance.setter
    # def balance(self, amount):
    #
    #     if not amount:
    #         raise ValueError("amount не может быть 0")
    #     elif amount > 0:
    #         self.__balance += amount
    #     elif amount < 0 and self.__balance >= amount:
    #         self.__balance -= amount
    #     else:
    #         raise ValueError("баланс меньше суммы списания")


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.deposit(self.get_balance() * self.interest_rate)
        return self.get_balance()


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)

    def withdraw(self, amount):
        self._BankAccount__balance -= amount  # не понял как достучаться до self.__balance, не используя хитрости
        return self.get_balance()


accaunt_igor = SavingsAccount("Igor")
accaunt_igor.deposit(500)
accaunt_igor.withdraw(100)
accaunt_igor.apply_interest()