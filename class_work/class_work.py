'''
first_string = "Aisha"
print(bool(first_string))
second_string = "Zainab"
print(bool(second_string))
third_string = ""
print(bool(third_string))
fourth_string = ""
print(bool(fourth_string))

num_one = 0
print(bool(num_one))
num_two = 0.0
print(bool(num_two))
num_three = False + 1
print(bool(num_three))
num_four = 2
print(bool(num_four))
'''

#Simple Calculator

print("""***************
1. Addition
2. Subtraction
3. Multiplication
4. Division
***************""")

#Addition
print("Enter two numbers to add");
first_number = input("Enter a number: \n")
second_number = input("Enter a number: \n")
result = float(first_number) + float(second_number)
print(f"{first_number} + {second_number} = {result}0")

#Subtract
print("Enter two numbers to Subtract");
first_number = input("Enter a number: \n")
second_number = input("Enter a number: \n")
result = float(first_number) - float(second_number)
print(f"{first_number} - {second_number} = {result}0")

#Multipy
print("Enter two numbers to Multiply");
first_number = input("Enter a number: \n")
second_number = input("Enter a number: \n")
result = float(first_number) * float(second_number)
print(f"{first_number} * {second_number} = {result}0") 

#Divide
print("Enter two numbers to Divide");
first_number = input("Enter a number: \n")
second_number = input("Enter a number: \n")
result = float(first_number) / float(second_number)
print(f"{first_number} / {second_number} = {result}0") 

#Exponential
print("Enter two numbers for exponential");
first_number = input("Enter a number: \n")
second_number = input("Enter a number: \n")
result = float(first_number) ** float(second_number)
print(f"{first_number} ** {second_number} = {result}0")

#Floor Division
print("Enter two numbers for floor division");
first_number = input("Enter a number: \n")
second_number = input("Enter a number: \n")
result = float(first_number) // float(second_number)
print(f"{first_number} // {second_number} = {result}0") 

