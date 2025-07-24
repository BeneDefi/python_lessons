accounts = [
     ["1001", "Joy", "Savings", 1500],
     ["1002", "David", "Current", 2000],
     ["1003", "Ruth", "Savings", 1000]
]

accounts.remove(accounts[1])
print(accounts)

account_name, account_type = accounts[1][1], accounts[1][2]
print(account_name, account_type) 

print(accounts[0][1:3])



