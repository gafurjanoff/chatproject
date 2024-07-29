import json
from chat import chat_create
from menu import home_page




# Load data from JSON files
with open('../data/sign_up.json', 'r') as read_file_sign:
    data = json.load(read_file_sign)

with open('../data/id_number.json', 'r') as read_file_id:
    id_data = json.load(read_file_id)

with open('../data/login.json', 'r') as read_file_login:
    login_data = json.load(read_file_login)



# Sign Up Function
def sign_up():

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    print('\n')

    sign_up_check = False

    for user in data["users"]:
        if user["Username"] == username and user["Password"] == password:
            print("Sign up failed! Already Signed Up🤐🤐\n")
            print(f"Please Login In Your Account\n")
            sign_up_check = True

    if sign_up_check:
        return home_page()

    else:
        num = id_data['id'] + 1
        id_data['id'] = num
        new_user = {
                    "First_Name": first_name.capitalize(),
                    "Last_Name": last_name.capitalize(),
                    "Username": username,
                    "Password": password,
                   }

        data["users"].append(new_user)  # Correctly append the new user to the list
        with open("../data/sign_up.json", "w") as write_file_sign:
            json.dump(data, write_file_sign, indent=4)

        with open("../data/id_number.json", "w") as write_file_id:
              json.dump(id_data, write_file_id, indent=4)
        print("Signed Up successfully!\n")
        print("Please Login In Your Account")
        return login()







# Login function
def login():

    attempts = 0

    while attempts <= 3:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        login_users = {
            "Username": username,
            "Password": password
        }
        login_check = False

        for login in data["users"]:
            if login["Password"] == password and login["Username"] == username:
                print('\n')
                print(f"{login['First_Name']}  {login['Last_Name']}, You logged in successfully!\n")

                full_name = login["First_Name"] + " " + login["Last_Name"]

                print(f'Now, Login your Chat!\n')
                login_check = True

        if login_check:
            login_data["logins"].append(login_users)
            with open("../data/login.json", "w") as write_file_logins:
                json.dump(login_data, write_file_logins, indent=4)
            return chat_create(full_name)

        else:
            print('\n')
            print(f"Login failed! Incorrect credentials.\n")
            print(f"Either you entered an invalid username or password\n")
            print(f"Please try again.\n")
            attempts += 1

    if attempts >= 3:
        print(f"You have tried more than 3 attempts")
        print("If you have forgotten your password, Please Sign Up and Try again.\n")
        return home_page()



