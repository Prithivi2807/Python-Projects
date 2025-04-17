phone = input("Phone: ")
digits_mapping = {
    "1": "one",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = "" 
for char in phone:
    # digits_mapping[
    output += digits_mapping.get(char, "!") + " "
print(output)   