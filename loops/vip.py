'''
vip = ["John", "Jerry", "Tom", "Dimka"]

user = input("Enter your name: ").capitalize()

for name in vip:
    if user == name:
        print("VIP")
        break
else:
    print("REGULAR")

for number in range(1,101):
    print(f"{number}. {number} * {number} = {number * number}")


for number in range(1,101):
    if number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

'''

students = {
    "S001": {"name": "John Doe", "age": 20, "score": 85},
    "S002": {"name": "Jane Smith", "age": 19, "score": 92},
    "S003": {"name": "Michael Brown", "age": 21, "score": 78},
    "S004": {"name": "Emily Davis", "age": 22, "score": 88},
    "S005": {"name": "Daniel Johnson", "age": 20, "score": 95},
    "S006": {"name": "Sarah Wilson", "age": 18, "score": 81},
    "S007": {"name": "David Lee", "age": 23, "score": 76},
}

user_age = int(input("Enter your age: "))

found = False

for student_id, info in students.items():
    if info["age"] == user_age:
        print(f"Match found: {info}")
        found = True

if not found:
    print("No students found with that age.")


















