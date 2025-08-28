list1 = [4, 9, 2, 7, 5]  
list2 = []  
list3 = [-5, -10, -3, -8, -1]

fruits = ["apple", "banana", "cherry", "orange"]  
numbers = [10, 20, 30, 40, 50]  
names = ["Alice", "Bob", "Charlie"]

def get_first_item(items):
	if len(items) != 0:
		return items[0]
	else:
		return "List is empty"

def get_max_number(number):
	if len(number) != 0:
		max_value = number[0]
		for num in number:
			if num > max_value:	
				max_value = num
		return max_value
	else:
		return "List is empty"
	"""if len(number) != 0:
		return max(number)"""

print(get_first_item(fruits))
print(get_max_number(list2))


