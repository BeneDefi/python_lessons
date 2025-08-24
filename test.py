
word = "pparrbbd"
'''
for i in range(0, len(word)):
    num = 0
    for a in range(0, len(word)):
        if word[i] == word[a]:
            num += 1
    if num == 1:
        print(word[i])
'''
dictionary = {}
new = []

for character in word:
	if character in dictionary:
		dictionary[character] += 1
	else:
		dictionary[character] = 1
for key in dictionary:
	if dictionary[key] == 1:
		new.append(key)

print(new[1])


print(input)


