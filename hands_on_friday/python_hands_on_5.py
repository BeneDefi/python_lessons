'''
print("Question One")

password = input("Enter Password: ")
confirm_password = input("Confirm Password: ")

if password == confirm_password:
    print("Password Match")
else:
    print("Password Mismatch")

print("---Addition---")
first_number = float(input("Enter A number: "))
second_number = float(input("Enter second number: "))
print(f"Your result is {first_number + second_number}")

result = first_number + second_number

scores = []
scores.append(result)

print(scores)

students = {}  

student_record = {
    "name": "John",
    "level": "400",
    "score": 80
}

student_record["score"] += 10

students.update(student_record)

print(students)
'''

score = float(input("Enter you score: "))

if score >= 70 and score <= 100:
	print("A")
elif score >= 60 and score < 70:
	print("B")
elif score >= 50 and score < 60:
	print("C")
elif score >= 45 and score < 50:
	print("D")
elif score >= 40 and score < 45:
	print("E")
elif score >= 0 and score < 40:
	print("F")
else:
	print("Invalid Input")





