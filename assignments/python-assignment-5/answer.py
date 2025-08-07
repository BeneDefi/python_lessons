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

user_input = input("\nPlease enter a command: ").lower()
is_verified = False

if user_input == "register":
    print("\n ---Register---")
    username = input("Enter username: ").strip().lower()
    if not username:
        print("Username cannot be empty.")
    if len(username) < 3:
        print("Username must be at least 3 characters long.")
    if " " in username:
        print("Username cannot contain spaces.")
    user_exists = any(user["username"] == username for user in user_data)
    if not user_exists:
          password = input("Enter password: ").lower()
          if not password:
             print("Password cannot be empty.")
          if len(password) < 4:
             print("Password must be at least 4 characters long.")
          balance = float(input("Enter balance: "))
          if balance < 0:
             print("Balance cannot be negative.")
          print("\n User Created Successfully...!!!")
          verification = input("Do you wish to verify? (Verification costs: 1500) yes or no: ").strip().lower()
          if verification not in ["yes", "no"]:
              print("Invalid input. Please enter 'yes' or 'no'")
          if verification == "yes":
            if balance >= 1500:
              is_verified = True
              balance = balance - 1500
              print("\nverification updated successfully")
              print(f"Your balance is:{balance}")
            else:
              print("Insufficent funds. Please top up. To be Verified")
          elif verification == "no":
            print(f"Dear User, you need to be verified for maximum user experience.")
          else:
            print(f"Invalid Input, You are not a verified user...!!!")    
          user_record = {
                "username":username,
                "password":password,
                "balance":balance,
                "is_verified":is_verified,
                        }
          user_data.append(user_record)
          print(f"""\n---User Data---""")
          for user in user_data:
              print(f"""
              Username: {user['username']}
              Password: {user['password']}
              Available Balance: {user['balance']}
              Is Verified: {user['is_verified']}
              """)
    else:
      print(f"\n user {username} already exists.")
elif user_input == "login":
    print("\n---login---")
    login_name = input("Enter your username: ").lower()
    login_password = input("Enter your password: ").lower()
    username_exists = any(user["username"] == login_name for user in user_data)
    userpassword_exists = any(user["password"] == login_password for user in user_data)
    if username_exists:
      if userpassword_exists:
        print("Login Successful!")
      else:
        print(f"password mismatch for {login_name}")
    else:
      print(f"user {login_name} does not exists") 
else:
    print(f"""\n
        {user_input} is Not a Valid command.
          choose one from available commands:
             enter "login" to login
             enter "register" to register 
         """)



