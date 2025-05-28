# if it's hot'
#         It's a hot day'
#         Drink plenty of water
# otherwise if its cold
#         It's a cold day'
#         Wear warm clothes
# otherwise
#         It's a lovely day'

climate_1 = input("How was the weather hot, cold or warm: \n ")


if climate_1 == "hot":
    hot = True
    cold = False
elif climate_1 == "cold":
    hot = False
    cold = True
else:
    hot = False
    cold = False

def climate(is_hot, is_cold):
    if is_hot:
        print("It's a hot day")
        print("Drink plenty of water")
    elif is_cold:
        print("It's a cold day")
        print("Wear warm clothes")
    else:
        print("It's a lovely day")
print("Enjoy your day")

climate(is_hot=hot, is_cold=cold)
