class Registeration:
    Tuition = 50000
    def __init__(self, firstname, lastname, amount):
        self.firstname = firstname
        self.lastname = lastname
        self.amount = amount
    
    def display(self):
        return f"""
        FirstName : {self.firstname}

        """
    def balance(self):
        return self.Tuition - self.amount
    
    def balance_check(self):
        if self.balance() < 50000:
            return f"Balance to pay {self.balance()}"
        else:
            return "Paid fully"   

joy = Registeration("Joy", "Hk", 20000)
print(joy.balance_check())
