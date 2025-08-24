import random
dice_rolls = int(input("How many times do you want to roll the dice? : "))
if dice_rolls > 0:
	while dice_rolls:
		print("Role the dice. y/n")
		dice = input(" :").lower()
		if dice == "y":
			dice_one = random.randint(1, 6)
			dice_two = random.randint(1, 6)
			print(f"{dice_one}, {dice_two}")
		elif dice == "n":
			print("Thank you for playing!")
			break
		else:
			print("Invalid Input.")
else:
	print("Invalid choice or not a number.")
