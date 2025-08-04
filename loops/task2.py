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

for customer in range(customer_no):
    name = input("Input your name: ")
    order_amount = float(input("Input amount: "))
    loyalty_card = bool(input("Do you have a loyalty card? (True/False): "))
    is_student = bool(input("Are you a student? (True/False): "))
   
    if loyalty_card == True:
        loyalty_discount = order_amount * 0.10
        order_amount = order_amount - loyalty_discount
        
        if order_amount >= 20000:
            extra_discount = order_amount * 0.05
            order_amount = order_amount - extra_discount
    else:
         if order_amount >= 20000:
            result = "Free Drink"

    if is_student == True:
        student_discount = order_amount * 0.05
        order_amount = order_amount - student_discount

    customer_record = {
        "name": name,
        "order_amount": order_amount,
        "loyalty_card": loyalty_card,
        "is_student": is_student
    }

    customers.append(customer_record)
    
    print(customers)
    print("\n--- Order Summary ---")
    '''
    print(f"Customer Name: {customers['name']}")
    print(f"Customer Order amount: {customers['order_amount']}")
    print(f"Customer Loyalty Card: {customers['loyalty_card']}")
    print(f"Customer is a Student: {customers['is_student']}")
    '''
