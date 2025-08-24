'''
numbers = [12, 75, 150, 180, 145, 525, 50]

for number in numbers:
	if number > 500:
		break
	elif number > 150:
		continue
	elif number % 5 == 0:
		print(number)

original_list = [1, 2, 3, 4, 5]
reversed_list = []

for item in original_list:
    reversed_list.insert(0, item) 

print(reversed_list)
'''

numbers = [12, 75, 150, 180, 145, 525, 50]
	
largest_number = numbers[0]

for number in numbers:
	if number > largest_number:
		largest_number = number
		print(largest_number)

'''
numbers = [10, 24, 76, 23, 12]
max_value = numbers  # Initialize with the first element

for number in numbers[1:]:  # Iterate through the rest of the list
    if number > max_value:
        max_value = number

print(max_value)  
'''

