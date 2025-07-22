'''
countries = ["Australia", "Malawi", "Russia", "USA", "Iran"]
print(countries)
movies = ["GOT", "Lord of the rings", "Vikings", "The Nun", "300"]
print(movies)
number = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
print(number)
profile = ["Teyei", 20, False, 6.3, "brown"]
print(profile) 
provision = ["Garri", "Rice", "Beans", "Yam"]
print(provision)
'''
'''
code = ["x", "H", "e", "z", "l", "l", "!", "p", "o", "-    ", "n", " ", "W", "@", "r", "d", "o", "#"]

hello = code[1] + code[2] + code[4] + code[4] + code[8]
print(hello)


w = code[-6]
o = code[-2]
r = code[-4]
l = code[4]
d = code[-3]
world = w + o + r + l + d
print(world)

word = hello + " " + world
print(word)

word = word[::-1]
print(word)

reverse = code[::-1]
print(reverse)
'''

grid = [
["The", "sky", "is"],
["full", "of", "stars"],
["shining", "bright", "tonight"]
]

print(grid[0][0] + " " + grid[0][1])
print(grid[0][0] + " " + grid[1][2] + " " + "are" + " " + grid[2][0])

second_row = grid[1]
print(second_row[::-1])










