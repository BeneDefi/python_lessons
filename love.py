
def start():
	while True:
		print("""
			1. Love
			2. Health
			3. Wealth
			""")
		choice = int(input("Enter your choice: "))
		print(all_functions(choice))

def all_functions(choice):
	if choice == 1:
		return "I Love Me."
	elif choice == 2:
		return "I Am Healthy."
	elif choice == 3:
		return "I am Wealthy beyound imaginations"
	else:
		return "Thank You God!"
	

start()
