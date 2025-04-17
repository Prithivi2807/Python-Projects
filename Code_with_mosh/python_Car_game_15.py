command = ""
started = False

while command.lower() != "quit":
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("car stopped.")
    elif command == "help":
        print("""
        start - to start the car"
        stop - to stop the car
        quit - to exit
              """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that...")



# print(">")

# def help():
#     print("start - to start the car" )
#     print("stop - to stop the car" )
#     print("quit - to exit")

# if command == "help":
#     print(help())
# else:
#     print("I don't understand that...")


# while True:
#     print(">")
#     command = str(input()).lower()
#     print(type command))

# # if command == "start":
# #     print("Car started...Ready to go!")
# # elif command == "stop":
# #     print("Car stopped.")
# # else:
# #     print

