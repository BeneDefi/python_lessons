#Question One

my_age = 28
pi = 3.41159
magic_number = my_age * 3 + pi % 7
print(magic_number)
print(f"My magic Number is {magic_number}. And the data type of my magic number is : ", type(magic_number))

#Question Two

secret_word = "PythonIsAmazing"

first_six = secret_word[0:6]
print(first_six)

middle_word = secret_word[6:8]
print(middle_word)

last_seven = secret_word[8:15]
print(last_seven)

'''
To reverse a string:
I don’t need to specify start or stop values leaving them blank tells Python to use the entire string.
I set the step to -1, which tells Python to go through the string from the end to the beginning.
So, the slicing [::-1] essentially says:
A step of -1 means "start from the end and move backwards."
Start at the end of the string and step backwards one character at a time until the beginning.
'''

#PythonIsAmazing
string_reversed_slicing = secret_word[::5]
print(string_reversed_slicing)

'''
The slicing format is generally written as "start:stop:step".
If you leave out start and stop, and only specify step as 2, it tells Python.
Go through the entire string, but pick every second character only.
So, using ::2:
Starts at the first character,
Skips the next one,
Takes the one after that,
Skips again, and so on.
'''
second_character = secret_word[::2]
print(second_character)


#Question Three

first_word = secret_word[0:6]
first_word = first_word.upper()
print(first_word)

last_word = secret_word[6:15]
last_word = last_word.lower()
print(last_word)

combined_words = first_word + last_word
print(combined_words)



