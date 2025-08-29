

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
			5. Most Expensive Product
			6. Total Potential Sales
			7. Exit
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
		action = int(input("Enter '1' to add and '2' to reduce quantity: "))
		update_stock(store, name, quantity, action)
	elif user_choice == 3:
		name = input("Enter product name to purchase: ").strip().lower()
		quantity = int(input("Enter quantity of products you wish to purchase: "))
		sell_product(store, name, quantity)
	elif user_choice == 4:
		display_inventory(store)
	elif user_choice == 5:
		most_expensive_product(store)
	elif user_choice == 6:
		total_potential_sales(store)
	elif user_choice == 7:
		terminate_session()
	else:
		print("Invalid Choice: Choose from 1 - 7.")


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


def update_stock(store, name, quantity, action):
	if name in store:
		if quantity <= 0:
			print("Quantity cannot be negative")
		else:
			if action == 1:
				store[name]["quantity"] += quantity
				print(f"Stock for {name.capitalize()} updated to {quantity}.")
				print(store)
			elif action == 2:
				if quantity > store[name]["quantity"]:
					print("Input quantity exceeds available quatity to reduce!")
				else:
					store[name]["quantity"] -= quantity
					print(f"Stock for {name.capitalize()} updated to {quantity}.")
					print(store)
			else:
				print("Inavild choice: Choose 1 OR 2.")
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

def most_expensive_product(store):
	highest_price = 0
	most_expensive = None
	for product_name, product_data in store.items():
		if product_data["price"] > highest_price:
			highest_price = product_data["price"]
			most_expensive = (product_name, product_data)
	if most_expensive:
		print(f"The most expensive product is '{most_expensive[0]}': {most_expensive[1]}")
	else:
		print("No products in store.")

def total_potential_sales(store):
	total = 0
	for total_value in store.values():
		total += total_value["price"] * total_value["quantity"]
	print(total)

def terminate_session():
	print("Terminating Session...")
	exit()
start()		
