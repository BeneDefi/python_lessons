'''
friends = int(input("Enter number of friends: "))
amount = float(input("Enter how much each person contributed: "))
charge = 200

if friends <= 0:
    print("Invalid Data")
elif amount <= 0:
    print("Invalid amount")
else:
    total_fare = charge * friends
    available_funds = amount * friends
    if total_fare == available_funds:
       print("Payment complete no change")
    elif total_fare > available_funds:
       print(f"Insufficient Balance you need addition of:", total_fare - available_funds)
    elif total_fare < available_funds:
       remainder = available_funds - total_fare
       print(f"Paid successfully with change of: {remainder:.2f}")
       print(f"Each friend will get a cashback of: {remainder / friends:.2f}")

number = input("Input a number from 1 - 7: ")

match number:
    case "1":
      print("Monday")
    case "2":
      print("Tuesday")
    case "3":
      print("Wednesday")
    case "4":
      print("Thursday")
    case "5":
      print("Friday")
    case "6":
      print("Saturday")
    case "7":
      print("Sunday")
    case _:
      print("Invalid input: Enter (1, 7)")
'''

student_name = input("Input Student Name: ")
student_score = float(input("Input Student Score: "))
student_record = {
"name": student_name,
"score": student_score,
}

match student_record:
    case {"name":student_name, "score":student_score}:
        if student_record["score"] >= 70 and student_record["score"] <= 100:
            grade = "A"     
            print(f"Dear {student_record['name']}, your grade is {grade}")
    case {"name":student_name, "score":student_score}:
        if student_record["score"] >= 60 or  student_record["score"] <= 70:
            grade = "B"
            print(f"Dear {student_record['name']}, your grade is {grade}")
    case {"name":student_name, "score":student_score}:
        if student_record["score"] >= 0 or  student_record["score"] <= 60:
            grade = "Fail"
            print(f"Dear {student_record['name']}, your grade is {grade}")
    case _:
        print("Invalid Data Input") 









