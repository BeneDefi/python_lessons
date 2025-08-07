user_data = []

print("""\n
  *---------------------------------------*
  |      Login and Register Portal        |
  |   ________________________________    |
  |  commands:                            |
  |   enter "login" to login              |
  |   enter "register" to register        |
  *---------------------------------------*
""")

user_record = {
     "username":"teyei",
     "password":"1234",
     "balance":20000,
     "is_verified":True,
  }
user_data.append(user_record)

user_input = input("\nPlease enter a command: ").strip().lower()
is_verified = False

if user_input == "register":
    if user_input == " ":
     print("\n ---Register---")
     username = input("Enter username: ").strip().lower()
      if username == " ":
        if len(username) < 2:
          user_exists = any(user["username"] == username for user in user_data)
          if not user_exists:
          else:
           print(f"\n user {username} already exists.")
        else:
          print("Username must be at least 3 characters long.") 
      else
        print("Username cannot be empty.")
    else:
      print("Commands cannot be empty.")

elif user_input == "login":
    if user_input == " ":
    
    else
      print("Commands cannot be empty.")
else:
    print(f"""\n
         {user_input} is Not a Valid command.
           choose one from available commands:
              enter "login" to login
              enter "register" to register 
          """)

