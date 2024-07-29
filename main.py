import time

from menu import login_page, home_page

def main():
    while True:
        choice = home_page()
        if choice == '1':
            from register import sign_up
            sign_up()
        elif choice == '2':
            from register import login
            login()
        elif choice == '3':
            exit()
        else:
            print("Invalid choice. Please select 1 for Sign Up or 2 for Login.")
            continue
def login_main(chat_code, chat_id, full_name):
    while True:
        choice = login_page()
        if str(choice) == '1':
            time.sleep(3)
            from chat import all_messages
            all_messages()
            time.sleep(5)
        elif str(choice) == '2':
            from chat import text_message
            time.sleep(3)
            text_message(chat_code, chat_id, full_name)
            time.sleep(3)
        elif str(choice) == '3':
            from chat import delete_message
            delete_message()
            time.sleep(3)
        else:
            time.sleep(3)
            print("You left the chat application.\n\n")
            exit()
            continue

if __name__ == "__main__":
    main()
