'''
names = ("John", "Joe", "Blessing")
print(type(names))
ages = (22, 33, 11, 99)
print(type(ages))
heights = (12.2, 34.4, 22.1)
print(type(heights))
cars = (["Mercedes", "Toyota", "Honda"], [12, 3.4, True])
print(type(cars))
colour = ("Blue",)
print(type(colour))
mutiple = (names, ages, heights, cars, colour, "Orange", 33, True, 22.5)
print(type(mutiple))
'''


cultures = [
("Ngas", "Ngas", "Bwan", "Pusdung", ("Funkaya", "Yala")),
("Berom", "Berom", "Gwote", "Nzem Berom", ("Ashui", "Shou")),
("Afizere", "Izere", "Tuwon masara", "Izere Day", ("Angrari", "Mavo")),
]

print(f"Greetings used by the second tribe is {cultures[1][-1][-1]}")

print(f"The {cultures[0][0]} people wear {cultures[0][-1][0]} and eat {cultures[0][2]}")

festival_name, popular_food, *others = cultures[2][3], cultures[2][2], cultures[2]
print(f"The popular food is {popular_food} and festival name is {festival_name}")

#cultures[0][1] = "English"




