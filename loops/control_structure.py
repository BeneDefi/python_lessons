'''
amount = float(input("Input goods amount: "))
percentage = 0
 
if amount == 50000:
    percentage = amount * 0.20
    amount = amount - percentage
elif amount >= 30000 and amount <= 50000:
    percentage = amount * 0.10
    amount = amount - percentage
elif amount >= 10000 and amount < 30000:
    percentage = amount * 0.05
    amount = amount - percentage
else:
    percentage = "Sorry No Discount"
    
total = {
"discount": percentage,
"total": amount,
}
 
print("\n---- Total----")
print(f"Discount: {total['discount']}")
print(f"Total: {total['total']}")

score = int(input("Input Your Score: "))

if score >= 250 and score <= 400:
    print("Eligible for Medicine")
elif score >= 200 and score <= 249:
    print("Eligible for Engineering or Science")
elif score >= 180 and score <= 199:
    print("Eligible for Education or Social Science")
elif score <= 180:
    print("Not eligible for admission this year")
else:
    print("Not a valid score")

x = int(input("Enter a number: "))
next_multiple = 1000 * (x // 1000)
print(next_multiple)   
'''
number = float(input("Enter a number: "))
numbers =  number%1000==0
balance = 10000

if number <= balance:
    if number > 0:
        if numbers == True:
            print("Withdrawal processing...")
            print(f"Balance: ", balance - number)
        else:
            print("You can only withdraw 1000 Notes.")
    else:
        print("Invalid Amount")
else:
    print("Insufficient funds")












                                      
