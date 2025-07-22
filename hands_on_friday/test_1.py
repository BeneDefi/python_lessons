#Question one
print("Question One")
print("Enter maximum of one hundred and fifty characters")
user_bio = input("Enter your bio:\n")
print(len(user_bio))
n = 20
print(user_bio[:n])
print(len(user_bio[-n:]))
print(user_bio[-n:])
print("**********")

#Question two
print("Question Two")
num_of_friends = input("Input number of friends:")
bill = input("Input the total bill:")
total_bill = float(bill) / int(num_of_friends)
print(f"Total Bill is {bill}. Each person should pay {total_bill}.")
print("**********")

#Question Three
print("Question Three")
movie = input("Input title of movie you've watched: \n")
times_watched = int(input("Input number of times you've watched the movie:\n"))
print(f"I have watched {movie} {times_watched} times")
print(movie.upper())
print(movie[-3:])
print("**********")

#Question Four
print("Question Four")
monday_steps = float(input("Input total steps covered on monday:"))
tuesday_steps = float(input("Input total steps covered on tuesday:"))
wednesday_steps = float(input("Input total steps covered on wednesday:"))
total_steps = monday_steps + tuesday_steps + wednesday_steps
total_steps_per_day = total_steps / 3
print(f"You have completed a total of {total_steps:,.2f} steps in three days. And completed an average of {total_steps_per_day:,.2f} steps a day.")
print("*********")

#Question five
print("Question Five")
password = input("Input password:")
print(len(password))

hashed_password =  password[0] + '*' * (len(password) - 2) + password[-1]

print(hashed_password)
print("*********")





