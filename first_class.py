#This Python script acts as a micro-wave
import time
print ('''
*****************
Cohort III Micro-wave
1. Open The Micro wave
2. Put the Rice
3. Set time
''')

customers = []
customer = {}

name = input("Enter your name:")
customer["name"] = name

time_to_micro_wave =input("Duration:\n")
customer["duration"] = time_to_micro_wave

convert_to_int=float(time_to_micro_wave)
price_to_pay = convert_to_int * 1000
customer["price"] = price_to_pay

print('You are to pay ₦', price_to_pay, "only")
print(f"Your Rice will be ready {convert_to_int} min(s) {name}")
print("4. I will let you know when its ready...")

customers.append(customer)

minutes_in_seconds=60
time.sleep(convert_to_int * minutes_in_seconds)
print(customer)
print("Your Food Is Ready")
print(customers)

