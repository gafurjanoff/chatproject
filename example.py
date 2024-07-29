import json
import random
import time

from menu import login_page
from main import login_main

with open('../data/sign_up.json', 'r') as read_file_sign:
    data = json.load(read_file_sign)

with open('../data/chat.json', 'r') as read_file_chats:
    chat_data = json.load(read_file_chats)
with open('../data/group_chat.json', 'r') as groupchat_read_file:
    group_chat = json.load(groupchat_read_file)


def chat_create():

    username = input("Enter Your  Username: ")
    password = input("Enter Your  Password: ")
    chatid = input("Enter Your Chat Id: ")
    chat_code = random.randint(100000, 999999)
    time.sleep(2)
    islogged = False
    for chat in chat_data["chats"]:
        if (chat["ChatID"] == chatid) and (chat["Username"] == username) and (chat["Password"] == password):
            print('\n')
            print(f"                 You Have Logged In Your Chat: {chat['ChatID']}\n")
            islogged = True

    login_page()
    print(f"                    Your chat_code: {chat_code} Don't share it with anyone!\n")

    if islogged:
        join_chat(chat_code, chatid)
    chats = {
        "ChatID": chatid,
        "Username": username,
        "Password": password
    }

    chat_data["chats"].append(chats)
    with open("../data/chat.json", "w") as write_file_chats:
        json.dump(chat_data, write_file_chats, indent=4)


def join_chat(chatid, chat_code) -> None:

    print('\n')
    print(f"                    Please Enter Your Enter Your Details To Send Your Message\n")
    chatid = input("Enter Your Chat Id: ")
    chat_code = input("Enter Your Chat Code: ")

    isjoined = False
    for chat in chat_data["chats"]:
        if (chat["ChatID"] == chatid):
            isjoined = True
            break

    if isjoined:
        login_main(chatid, chat_code)

    else:
        print("\n")
        print(f"              First, Please Create The Chat!\n")
        return chat_create()


def all_messages():
     print(f"""  
                      Chat_ID: {group_chat['Chat_ID']}\n  
                      Chat_Code: {group_chat['Chat_Code']}
                      Messages: {group_chat['Messages']}""")

def text_message(chatid, chat_code):

        message = input("Enter your message: ")
        print(f"""  
                  Chat_ID: {chatid}\n  
                  Message: {message}""")

        group_chat["messages"].append({
            "Chat_ID": chatid,
            "Chat_Code": int(chat_code),
            "Message": message
        })
        with open("../data/group_chat.json", 'w') as groupchat_write_file:
            json.dump(group_chat, groupchat_write_file, indent = 4)




