# Expected username and password (you can change the value)
correct_username = "user"
correct_password = "pass"
admin_username = "admin"
admin_password = "admin"

# Enter username and password
username_input = input("Please provide username: ")
password_input = input("Please provide password: ")

#correct_user_pw = user_na == "user" and correct_password == "pass"
#correct_admin_user_pw = admin_username == "admin" and admin_password == "admin"

# TODO: Notify user if credentials are valid or invalid
correct_credentials = (username_input == "user" and password_input == "pass") or (username_input == "admin" and password_input == "admin")
if correct_credentials:
    print("Access Granted")
else:
    print("Access Denied")

