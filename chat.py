import json
import random
from menu import login_page

with open('../data/sign_up.json', 'r') as read_file_sign:
    data = json.load(read_file_sign)

with open('../data/chat.json', 'r') as read_file_chats:
    chat_data = json.load(read_file_chats)

with open('../data/group_chat.json', 'r') as groupchat_read_file:
    group_chat = json.load(groupchat_read_file)


def chat_create(full_name):

    username = input("Enter Your Username: ")
    password = input("Enter Your Password: ")
    chatid = input("Enter Your Chat Id: ")

    chat_code = random.randint(100000, 999999)

    islogged = False
    for chat in chat_data["chats"]:
        if (chat["ChatID"] == chatid) and (chat["Username"] == username) and (chat["Password"] == password):
            print('\n')
            print(f"You Have Logged In Your Chat: {chat['ChatID']}\n")
            islogged = True
            break

        else:
            chats = {
                "ChatID": chatid,
                "Username": username,
                "Password": password
            }
            chat_data["chats"].append(chats)
            with open("../data/chat.json", "w") as write_file_chats:
                json.dump(chat_data, write_file_chats, indent=4)
            print('\n')
            print(f"Your Chat Has Been Created Successfully.\n")
            print(f"Your chat_code: {chat_code} Don't share it with anyone!")
            return join_chat(chat_code, chatid, full_name)





    if islogged:
        print('\n')
        print(f"Your Chat Has Been Created Successfully.\n")
        print(f"Your chat_code: {chat_code} Don't share it with anyone!\n")
        return join_chat(chatid, chat_code, full_name)




def join_chat(chat_code, chat_id, full_name) -> None:
    print('\n')
    print(f"Please Enter Your Details To Send Your Message\n")
    entered_chatid = input("Enter Your Chat Id: ")
    entered_chat_code = input("Enter Your Chat Code: ")

    isjoined = False
    for chat in chat_data["chats"]:
        if chat["ChatID"] == entered_chatid:
            isjoined = True
            break

    if isjoined:
        from main import login_main  # Importing locally to avoid circular imports
        login_main(entered_chat_code, entered_chatid, full_name)
    else:
        print("\n")
        print(f"First, Please Create The Chat!\n")
        return chat_create()


def all_messages():

    for message in group_chat['messages']:
        print(f"""  
                                                Chat_ID: {message["Chat_ID"]} 
                                                Chat_Code: {message["Chat_Code"]}\n
                                                Messages: {message["Message"]}""")


def text_message(chat_code, chat_id, full_name):
    message_seen = False
    message = input("Enter your message: ")
    print(f"""  
                                          Full_Name: {full_name}
                                          Chat_ID: {chat_id}\n  
                                          Message: {message}""")

    group_chat["messages"].append({
        "Chat_ID": chat_id,
        "Chat_Code": chat_code,
        "Message": message
    })
    with open("../data/group_chat.json", 'w') as groupchat_write_file:
        json.dump(group_chat, groupchat_write_file, indent=4)


def delete_message():
    chatid = input("Enter Your Chat ID: ")
    message_to_delete = input("Enter the message you want to delete: ")

    message_found = False
    for message in group_chat["messages"]:
        if message["Chat_ID"] == chatid and message["Message"] == message_to_delete:
            group_chat["messages"].remove(message)
            message_found = True
            break

    if message_found:
        with open("../data/group_chat.json", 'w') as groupchat_write_file:
            json.dump(group_chat, groupchat_write_file, indent=4)
        print("Message deleted successfully.")
    else:
        print("Message not found. Please check your Chat ID and the message content.")
