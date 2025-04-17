customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
} # dictionary

customer["name"] = "Jack Smith"
print(customer.get("birthdate")) # If the get method was called if the value are not present it will give you None 
                                    ## if the values are present it will generate print the value. 
# print(customer.get("birthdate", "Jan 1 1980"))

customer["birthdate"]  = "Jan 1 1980"
print(customer["birthdate"])
