# Personal Account Management System

This is a simple Python project that simulates a personal account management system. It allows you to deposit and withdraw money from an account while keeping track of transactions. The system works by storing transaction history and calculating the account balance.

## Files in the Project

- **`Amount.py`**: This file contains the `Amount` class. The `Amount` class defines a transaction with an amount, transaction type (deposit or withdrawal), and the timestamp when the transaction occurred.
- **`PersonalAccount.py`**: This file contains the `PersonalAccount` class. It represents a personal bank account that stores details such as account number, account holder name, balance, and transaction history.
- **`main.py`**: This is the entry point of the program. It creates an instance of `PersonalAccount` and allows the user to deposit and withdraw money, as well as print transaction history.

## Purpose

This system is meant to simulate basic banking functions such as:
- Making deposits and withdrawals
- Storing transaction history
- Displaying the account balance and transaction history

## How It Works

1. **Creating a Personal Account**: You create an account by providing the account number, account holder's name, and initial balance.
2. **Depositing Money**: You can deposit money into your account. Every deposit is recorded with the transaction type as "deposit".
3. **Withdrawing Money**: You can withdraw money from your account. Every withdrawal is recorded with the transaction type as "withdraw".
4. **Transaction History**: You can view the history of your transactions, including deposits and withdrawals, with their timestamps.

---

## UML
![](https://i.ibb.co/Y41fvdJq/123123.jpg)
