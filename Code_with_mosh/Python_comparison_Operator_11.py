# # if temperatore is greaterthan 30 
# #     it's a hot '
# # otherwise if it's less than 10'
# #     it's a cold day'
# # otherwise
# #     it's neither hot nor cold'
# # # celcius not faranite

# temperature = 30 
# if temperature > 30:
#     print("Its a hot day")
# elif temperature < 10:
#     print("It's a cold day")
# else:
#     print("it's neither hot nor cold")

# if name is less than 3 characcters long 
#     name must be at least 3 characters
# otherwise if it's more than 50 characters long'
#     name can be a maximum of 50 characters
# otherwise
#     name looks good!

# Solution 
name = input("give me only text: \n")
if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good!")