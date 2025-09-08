import random

class Bank:
    promo_prize = 2000

    def __init__(self, acc_name, amount, has_prize=False, subscribed_sms=False, subscribed_email=False):
        if has_prize:
            amount += self.promo_prize
        self.name = acc_name
        self.acc_num = random.randint(100, 900)
        self.balance = amount
        self.is_frozen = False  
        self.subscribed_sms = subscribed_sms
        self.subscribed_email = subscribed_email

    def deposit(self, amount):
        if self.is_frozen:
            print(f"Account {self.name} is frozen. Cannot deposit.")
            return
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
            self.message(f"You have deposited {amount}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if self.is_frozen:
            print(f"Account {self.name} is frozen. Cannot withdraw.")
            return
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
            self.message(f"You have withdrawn {amount}.")

    def transfer(self, recipient_account, amount):
        if self.is_frozen:
            print(f"Account {self.name} is frozen. Cannot transfer.")
            return
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
            self.message(f"You have transferred {amount} to {recipient_account.name}.")
            recipient_account.message(f"You have received {amount} from {self.name}.")

    def freeze(self):
        self.is_frozen = True
        print(f"Account {self.name} has been frozen.")

    def unfreeze(self):
        self.is_frozen = False
        print(f"Account {self.name} has been unfrozen.")

    def message(self, msg):
        if self.subscribed_sms and self.subscribed_email:
            print(f"[SMS & Email to {self.name}]: {msg}")
        elif self.subscribed_sms:
            print(f"[SMS to {self.name}]: {msg}")
        elif self.subscribed_email:
            print(f"[Email to {self.name}]: {msg}")
        else:
            print(f"[No message sent to {self.name}]")

jane = Bank("Jane", 1000, has_prize=False, subscribed_sms=True)
joy = Bank("Joy", 2000, has_prize=True, subscribed_sms=True, subscribed_email=True)

joy.deposit(300)
joy.withdraw(1000)
joy.transfer(jane, 1000)

joy.freeze()
joy.withdraw(100) 
joy.unfreeze()
joy.withdraw(100) 

print(f"Joy's final balance: {joy.balance}")
print(f"Jane's final balance: {jane.balance}")
