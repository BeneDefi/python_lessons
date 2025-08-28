

store = {
"laptop": {"price": 1200, "quantity": 5},
"headphones": {"price": 150, "quantity": 10},
"mouse": {"price": 40, "quantity": 20},
}

def start():
	while True:
		print("""\n Online Store Inventory & Sales System
			1. Add Product.
			2. Update Stock.
			3. Sell Product.
			4. Display inventory.
			5. Exit
			""")
		user_choice = int(input("Enter choice: "))
		all_functions(user_choice)

def all_functions(user_choice):
	if user_choice == 1:
		name = input("Enter product name: ").strip().lower()
		price = float(input("Enter product price: "))
		quantity = int(input("Enter product quantity: "))
		add_product(store, name, price, quantity)
	elif user_choice == 2:
		name = input("Enter product name to be updated: ").strip().lower()
		quantity = int(input("Enter quantity to update: "))
		update_stock(store, name, quantity)
	elif user_choice == 3:
		name = input("Enter product name to purchase: ").strip().lower()
		quantity = int(input("Enter quantity of products you wish to purchase: "))
		sell_product(store, name, quantity)
	elif user_choice == 4:
		display_inventory(store)
	elif user_choice == 5:
		terminate_session()
	else:
		print("Invalid Choice: Choose from 1 - 5.")


def add_product(store, name, price, quantity):
	if name in store:
		print(f"Error: {name.capitalize()} already exsist in store! \nUpdate {name.capitalize()} in store.")
	else:
		if not name.strip() or len(name.strip()) < 2:
			print("Error: Product name cannot be empty or less than 2 characters long!")
		elif price <= 0 or quantity <= 0:
			print("Error: Price and quantity must be greater than 0!")
		else:
			store[name] = {
				"price": price,
				"quantity": quantity
			}
			print(f"{name.capitalize()} added successfully!")
			print(store)


def update_stock(store, name, quantity):
	if name in store:
		if quantity <= 0:
			print("Quantity cannot be negative")
		else:
			store[name]["quantity"] = quantity
			print(f"Stock for {name.capitalize()} updated to {quantity}.")
			print(store)
	else:
		print(f"Sorry {name.capitalize()} not in store to update!")

def sell_product(store, name, quantity):
	if name in store:
		if quantity <= 0:
			print("Quantity must be greater than zero.")
		elif quantity <= store[name]["quantity"]:
			store[name]["quantity"] -= quantity
			total = store[name]["price"] * quantity
			print(f"Sold {quantity} x {name.capitalize()} successfully!")
			print(f"The total price to be paid for {quantity} quantity of {name.capitalize()} is {total:.2f}")
			return total
		else:
			print("Error: Exceeding quantity in store!")
	else:
		print(f"Sorry {name.capitalize()} is not in store!")

def display_inventory(store_dict):
	print("\n---Inventory---")
	for product_name, product_data in store_dict.items():
		print(f"Product Name: {product_name.capitalize()} : Product Price :{product_data['price']:.2f}, Product Quantity :{product_data['quantity']} ")

def terminate_session():
	print("Terminating Session...")
	exit()
start()		
