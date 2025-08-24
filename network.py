print("""
Welcome To Bolt Swap.
The Universal Money Bridge.
Connects crypto and local banks.
Choose from availabe options.
1. Transfer/Swap
2. History
3. Earn 'Hot'
	""")

history = []
counts = 10


while counts:
	options = int(input("Input from available options: 1, 2, 3 \n:"))
	if options == 1 and options.isdigit():
		print("---Transer/Swap---")
	elif options == 2 and options.isdigit():
		print("---History---")
	elif options == 3 and options.isdigit():
		print("---Earn 'Hot'---")
	else:
		print("Invalid")






