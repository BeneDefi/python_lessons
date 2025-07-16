'''
first_name = "python"
first_letter = first_name[0].upper() + first_name[1:]
print(first_letter)
print(first_name.title())
print(first_name.capitalize())
'''

email = "user@domain.com"
gmail = "gmail"
email = email[0:5] + gmail + email[11:]
print(email)

word = "abcdefghijk"

first_half = word[:len(word)//2]
second_half = word[len(word)//2 + len(word)%2:]

print(first_half)
print(second_half)

wordLenght = len(word) // 2

first = word[:wordLenght]
second = word[wordLenght:]



