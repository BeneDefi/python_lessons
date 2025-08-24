"""
Assignment Question 
1. Write a function check_even_odd(n) that takes an integer n and returns: 
"Even" if the number is even, 
"Odd" if the number is odd. 
Function with Default Arguments & Loops 
2. Write a function count_vowels(text, vowels="aeiou") that counts how many 
vowels appear in a given text. 
Example: count_vowels("Python is fun") should return 3. 
Function with Conditions and List 
3. Write a function count_even(numbers) that counts how many even numbers are 
in a list. 
Example: count_even([1, 2, 3, 4, 6]) → 3 
4. Write a function triangle_area(base, height) that calculates 
the area of a triangle using the formula: 
Area=1/2×base×height 
Example: triangle_area(10, 5) → 25.0 
5. Write a function called check_password_strength that takes a 
password string and returns "Weak", "Medium", or "Strong" 
based on these criteria: Weak (less than 6 characters), Medium 
(6-10 characters), Strong (more than 10 characters and 
contains both letters and numbers).
"""

def check_even_odd():
	num = int(input("Enter an integer: "))
	if num % 2 == 0:
		print(f"{num} is an even number")
	else:
		print(f"{num} is an odd number")

#check_even_odd()


def count_vowels():
	word = input("Enter a word: ").lower()
	vowels = ["a","e","i","o","u"]
	count = 0
	for vowel in vowels:
		if vowel in word:
			count +=1
	print(f"There are {count} vowel(s) in {word}")

#count_vowels()

def count_even(numbers):
	count = 0
	for num in numbers:
		if num % 2 == 0:
			count +=1
	print(f"There are {count} even number(s)")

#count_even([1,3,5,7,8,4,6])

def triangle_area(base, height):
	area = 1/2 * base * height
	print(area)

#triangle_area(10, 5)

def check_password_strenght():
	password = input("Enter password: ").strip()
	word_flag = False
	number_flag = False

	for i in password:
		if i.isalpha():
			word_flag = True
		if i.isdigit():
			number_flag = True

	if password != " ":
		if len(password) <= 6:
			print("Password is weak")
		elif len(password) >= 6 and len(password) <= 10:
			print("Password strenght medium")
		elif len(password) >= 10 and word_flag and number_flag:
			print("Your password strenght is strong")


check_password_strenght()
