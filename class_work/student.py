student_record = []
num_of_student = 3

def add_student():
	student_id = 1
	for _ in range(num_of_student):
		student_name = input("Enter your name: ").lower().strip()
		student_age = int(input("Enter your age: "))
		student_level = input("Enter your level: ").strip()
		student_score = float(input("Enter your score: "))
		if student_id == student_id:
			student_data = {
					"student_id":student_id,
					"name": student_name,
					"age": student_age,
					"level": student_level,
					"score": student_score,
					}
		student_record.append(student_data)
		student_id += 1

add_student()
print(student_record)

def delete_student():
    del_student = int(input("Enter the student ID you wish to delete: "))
    found = False
    for student in student_record:
        if student["student_id"] == del_student:
            student_record.remove(student)
            print(f"Student with ID {del_student} has been removed.")
            found = True
            break
    if not found:
        print(f"No student found with ID {del_student}.")



