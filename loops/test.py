students_data = []

print("--Student Profile--")
print("""\n---Available Options---
Choose from available options: 1 or 2.
1. Register.
2. Login.
    """)

options = int(input("Choose from available options: "))
while True:
	if options == 1:
		print("Register")
		name = input("Enter your name: ").strip().upper()
		if name != "" and name != "  ":
			if len(name) >= 3:
				gender = input("Enter Your Gender: \nchoose 'male' or 'female': ").strip().lower()
				if gender == "male" or gender == "m" or gender  == "female" or gender == "f":
					print("done")
					break
				else:
					print("Invalid Option:\nChoose 'M' or 'f'")
			else:
				print("Name must be atleast three charaters long.")
		else:
			print("Name field cannot be empty.") 
		continue
	elif options == 2:
		print("Login")
		continue
	else:
		print("Wrong option selected: Choose from options available 1 or 2.")
		options = int(input("Choose from available options: "))
