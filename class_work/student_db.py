students_db = {}

def start():
	while True:
		print("""
		1. Add Student
		2. Delete Student
		3. Update Student Record
		4. Get Student Record
		5. Display all Student Record
		6. Search Student username
		7. Display total number of students
		8. Filter By Age
		0. Terminate Session		
		""")
		user_choice = int(input(""))
		if user_choice == 0:
			print("Exiting...")
			print("Thank You!😄🥂")
			break
		elif user_choice == 1:
			add_student()
			print("I am back to the start function")
		elif user_choice == 2:
			delete_student()
		elif user_choice == 3:
			update_student()
		elif user_choice == 4:
			get_student()
		elif user_choice == 5:
			get_students()
		elif user_choice == 6:
			search_student_by_name()
		elif user_choice == 7:
			count_students()
		elif user_choice == 8:
			filter_by_age()
		else:
			print("Invalid Choice.")


def add_student():
	print("I am executing add student logic")
	name = input("Student name: ").lower()
	age = int(input("Student age: "))
	department = input("Department: ")
	key = len(students_db) + 1
	students_db[key] = {"name":name, "age":age, "dept":department}
	print(students_db)

def delete_student():
	student_id = int(input("Student ID to delete: "))
	if student_id in students_db:
		del students_db[student_id]
		print(f"Student with ID {student_id} deleted successfully")
	else:
		print("ID not found!")

def update_student():
	student_id = int(input("Enter student ID: "))
	if student_id in students_db:
		print("""
			Choose what you wish to update:
			1. Name
			2. age
			3. Department
			""")
		choice = int(input(""))
		if choice == 1:
			student_name = input("Enter name you wish to update: ")
			students_db[student_id]["name"] = student_name
		elif choice == 2:
			student_age = int(input("Enter age to update: "))
			students_db[student_id]["age"] = student_age
		elif choice == 3:
			student_dept = input("Enter department to update: ")
			students_db[student_id]["dept"] = student_dept
		else:
			print("Invalid Choice")
		print(students_db)
	else:
		print("ID not found")

def get_student():
	student_id = int(input("Enter Student ID: "))
	if student_id in students_db:
		student = str(student_db[student_id])
		student = student[1:-1]
		print(f"The user id is: {student}")
	else:
		print("ID Not Found")


def get_students():
	for student in students_db.values():
		student = str(student)
		student = student[1:-1]
		print(student)

def search_student_by_name():
	search_name = input("Enter name to search: ").lower()
	found = False
	for student_id, student_data in students_db.items():
		if search_name in student_data["name"]:
			print(f"ID: {student_id}, Name: {student_data['name']}, Age: {student_data['age']}, Department: {student_data['dept']}")
			found = True	

	if not found:
			print("No student found with that name.")

def count_students():
	print(f"Total number of verified registered students are: ", len(students_db))

def filter_by_age():
	student_age = int(input("Enter age to filter: "))
	found = False
	for student_id, student_data in students_db.items():
		if student_age < student_data["age"]:
			print(f"ID: {student_id}, Name: {student_data['name']}, Age: {student_data['age']}, Department: {student_data['dept']}")
			found = True

	if not found:
		print("No student found")

	
start()
