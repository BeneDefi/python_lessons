"""
Task 2: Smart Restaurant Discount System
 
You are helping a restaurant in Jos implement an automated discount system for their weekend promo.
 
The rules are:
1. Customers with a loyalty card get a 10% discount.
2. If the customer's order amount is above 20,000 NGN:
     - Loyalty card holders get an additional 5% discount.
     - Non-loyalty card holders get a free soft drink instead.
3. Students (verified with student ID) get an extra 5% discount on top of whatever they qualify for.
 
Customer data is stored in a dictionary like this:
 
customer = {
     "name": "Godiya",
     "order_amount": 25000,
     "loyalty_card": True,
     "is_student": False
 }
 
Write a nested if-else block that:
1. Calculates the final discount or freebie for the customer.
2. Stores the result in a dictionary called `order_summary`.
3. Prints out a summary for the cashier.
"""

customers = []
customer_no = 3

for _ in range(customer_no):
    name = input("Input your name: ")
    order_amount = float(input("Input amount: "))

    loyalty_card_input = input("Do you have a loyalty card? (yes/no): ").strip().lower()
    loyalty_card = loyalty_card_input == "yes"

    student_input = input("Are you a student? (yes/no): ").strip().lower()
    is_student = student_input == "yes"

    original_amount = order_amount 
    discounts = 0.0
    freebie = None

    if loyalty_card:
        discount = order_amount * 0.10
        discounts += discount
        order_amount -= discount

        if original_amount > 20000:
            extra_discount = order_amount * 0.05
            discounts += extra_discount
            order_amount -= extra_discount
    else:
        if original_amount > 20000:
            freebie = "Free Soft Drink"

    if is_student:
        student_discount = order_amount * 0.05
        discounts += student_discount
        order_amount -= student_discount

    order_summary = {
        "name": name,
        "original_amount": original_amount,
        "final_amount": round(order_amount, 2),
        "loyalty_card": loyalty_card,
        "is_student": is_student,
        "total_discount": round(discounts, 2),
        "freebie": freebie
    }

    customers.append(order_summary)

    print("\n--- Order Summary ---")
    print(f"Customer Name: {order_summary['name']}")
    print(f"Original Order Amount: ₦{order_summary['original_amount']}")
    print(f"Total Discount: ₦{order_summary['total_discount']}")
    print(f"Final Amount to Pay: ₦{order_summary['final_amount']}")
    print(f"Loyalty Card Holder: {order_summary['loyalty_card']}")
    print(f"Student: {order_summary['is_student']}")
    if freebie:
        print(f"Freebie: {order_summary['freebie']}")
    print("------------------------\n")

# print(customers)









