
def start():
	while True:
		print("""
			1. Love
			2. Health
			3. Wealth
			""")
		choice = int(input("Enter your choice: "))
		all_functions(choice)

def all_functions(choice):
	if choice == 1:
		print("I Love Me.")
	elif choice == 2:
		print("I Am Healthy.")
	elif choice == 3:
		print("I am Wealthy beyound imaginations")
	else:
		print("Thank You God!")
	

start()
