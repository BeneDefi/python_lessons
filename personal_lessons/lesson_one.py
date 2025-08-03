'''
Write a function to split the restaurant bill among friends.

Take the subtotal of the bill and the number of friends as inputs.
Calculate the total bill by adding 20% tax to the subtotal and then divide it by the number of friends.
Return the amount each friend has to pay, rounded off to two decimal places.
'''

bill = float(input("Input Bill: "))
friend = int(input("Input Number of friends: "))
percentage = bill * 0.20
bill += percentage
bill /= friend
print(f"Each friend will pay {bill :.2f}")

'''
Write a function to check whether a student passed or failed his/her examination.

Assume the pass marks to be 50.
Return Passed if the student scored more than 50. Otherwise, return Failed.
'''

pass_mark = float(input("Input your score: \n"))
result = "pass" if pass_mark >= 50 else "Failed"
print(result)



