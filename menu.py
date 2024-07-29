
def home_page():
    print('\n')
    print(f"                                 Welcome To FiftyGram\n")
    print(f"                                 1.Register\n"
          f"                                 2.Login\n"
          f"                                 3.Logout\n")

    print("         Choose One Option 1 or 2")
    choice = input(">>>>>>>>>> ")
    return choice

def login_page():

    print(f"\n")
    print(f"                                  Welcome to FiftyGram  Chat Group!\n")
    print(f"                                  This Is A Sectret Group Chat\n")
    print(f"                                  Don't Hesitate When Sharing Your Opinions\n")

    print(f"                                  1. See All Chats")
    print(f"                                  2. Text Message")
    print(f"                                  3. Delete Your Chat")
    print(f"                                  4. Log out Chat\n")
    print("         Choose One Of The Options")
    chois = int(input(">>>>>>  "))
    return chois
