import random

class Bank:
    promo_prize = 2000
    def __init__(self, acc_name, amount, has_prize = False):
        if has_prize:
            amount += self.promo_prize
        self.name = acc_name
        self.acc_num = random.randint(100, 900)
        self.balance = amount
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def transfer(self, recipient_account, amount):
        if amount <= 0:
            print("Transfer amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            recipient_account.balance += amount
            print(f"Transferred {amount} from {self.name} to {recipient_account.name}.")
            print(f"{self.name}'s new balance: {self.balance}")
            print(f"{recipient_account.name}'s new balance: {recipient_account.balance}")

        
jane = Bank("Jane", 1000, False)

joy = Bank("Joy", 2000, True)
joy.deposit(300)
joy.withdraw(1000)
joy.transfer(jane, 1000)
print(joy.balance)