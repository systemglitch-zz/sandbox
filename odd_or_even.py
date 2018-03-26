user_num = "start"
while user_num != "stop":
    user_num = input("Please provide a number: ")

    if int(user_num) % 2 == 0:
        print("your number is even")
    else:
        print("your number is odd")
