'''
students = []
student_num = 3

for student in range(student_num):
	name = input("Enter Your name: ")
	gender = input("Enter Your gender choose: M/F: ").lower()
	if gender == "m" or gender == "f":
		score = float(input("Enter Your Score: "))
		student_data = {
			"name":name,
			"gender":gender,
			"score":score
			}
		students.append(student_data)
	else:
		print("use on 'M' for male and 'F' female")
		break
print(students)

orders = [
    {"order_id": 101, "customer": "John", "items": 3, "total_price": 75},
    {"order_id": 102, "customer": "Mary", "items": 10, "total_price": 180},
    {"order_id": 103, "customer": "Alex", "items": 2, "total_price": 50},
    {"order_id": 104, "customer": "Grace", "items": 15, "total_price": 600},
    {"order_id": 105, "customer": "Paul", "items": 5, "total_price": 145}
]

for order in orders:
	if order["items"] >= 5:
		print(f"Customer Name: {order['customer']} and total price: {order['total_price']}")
	if order["total_price"] > 140 and order["total_price"] < 200:
		continue
	elif order["total_price"] > 500:
		break

posts = [
{"post": "Hello"},
{"post": "welcome"},
{"post": "How are you?"}
]

for post in posts:
	if post["post"] == "welcome":

number = 1
while number <= 100:
	if number % 2 != 0:
		print(f"Number: {number}")
	number +=1
'''


students = {
    "John": 60,
    "Mimi": 50,
    "Sarah": 30
}

keys = list(students)
length = len(keys)
count = 0

while count < length:
    key = keys[count]
    print(key, students[key])
    count += 1























