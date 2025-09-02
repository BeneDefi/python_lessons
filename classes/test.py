def add_list(numbers):
	result = 0
	for number in numbers:
		result += number
	return result
# print(add_list([2,2]))

def  bank_account(owner, *transactions, **details):
    print(owner)
    result = 0
    for transaction in transactions:
        result += transaction 
    print(f"Balance: {result}")
    for key, value in details.items():
        details[key] = value
    print(details)

# bank_account("John", 200, -50, 100, account_type = "Savings", branch = "Lagos")

def register_event(event_name, *participants, **details):
    
    print(f"Event name: {event_name}")
    print(f"Participants: {participants}")
    print(f"Details: {details}")

register_event("Tech Companies", "Alice", "Bob", "Charles", location ="Abuja", Date ="10th Sept", Organizers ="FiliBus")