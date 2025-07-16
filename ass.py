#Use input to get users: Full Name, Age, Height, Hobbies, IsMarried

print("Fill in Your Data")

fullName=input("Input your full Name: \n")

age=input("Input your age: \n")
age=int(age)

hobbies = input("Enter your hobbies (separated by commas): \n")
hobbies_list = hobbies.split(",")

height=input("Input your heigh: \n")
height=float(height)

isMarried=input("Are you married? yes/no: \n")

if isMarried.lower() == "yes":
    isMarried = True
elif isMarried.lower() == "no":
    isMarried = False
else:
    print("Input Yes or No")
    isMarried=None


print(f"Welcome {fullName}!", {type(fullName)})
print(f"Your age:{age}", {type(age)})
print(f"Your height:{height}", {type(height)})
print(f"Marital Status: {isMarried}", {type(isMarried)})
print(f"Your hobbies: {hobbies_list}", {type(hobbies_list)})
