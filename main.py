from amount import Amount
from PersonalAccount import PersonalAccount

if __name__ == "__main__":
    acc1 = PersonalAccount(23, "bmw", 0, [])
    acc1.deposit(Amount(100, "deposit"))
    print(acc1.get_balance())
    acc1.withdraw(50)
    print(acc1.get_balance())
    acc1.print_transaction_history()
    acc1.set_account_number(777)
    acc1.set_account_holder('Madina Gabbazova')
    print(acc1)