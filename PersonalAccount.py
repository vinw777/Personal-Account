from amount import Amount
class PersonalAccount:
    def  __init__(self, account_number : int , account_holder : str, balance : float, transactions : list ):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self._balance = 0.0
        self.transactions = transactions

    def deposit(self, amount):
        transaction = Amount(amount, "deposit")
        self._balance += amount.amount
        self.transactions.append(transaction)
        print(f"Deposited {amount.amount}")

    def withdraw(self, amount):
        transaction = Amount(amount, "withdraw")
        self._balance -= amount
        self.transactions.append(transaction)
        print(f"Withdrawed {amount}")

    def print_transaction_history(self):
        for transaction in self.transactions:
            print(f"{transaction.transaction_type}: {transaction.amount}")

    def get_balance(self):
        return self._balance
    def get_account_number(self):
        return self.__account_number
    def set_account_number(self, account_number):
        self.__account_number = account_number
    def get_account_holder(self):
        return self.__account_holder
    def set_account_holder(self, account_holder):
        self.__account_holder = account_holder

    def __str__(self):
        return f"{self.__account_number}, {self.__account_holder}, {self._balance}"

    def __add__(self, amount):
        self.deposit(amount)
        return self
    def __sub__(self, amount):
        self.withdraw(amount)
        return self
