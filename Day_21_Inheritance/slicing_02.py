piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ("do", "re", "mi", "fa", "so", "pr", "la", "ve")

print(piano_keys[2:5])
print(f"print last 1st to all 5 {piano_keys[1:5]}")
print(f"print last all 5 position {piano_keys[:5]}")
print(f"print the numbers in between the range of 2 digits with the increment of 2 {piano_keys[2:5:2]}")
print(f"print everything in the list of 2nd items{piano_keys[::2]}")
print(f"reverse this list for us {piano_keys[::-1]}")
print(f"tuple also same commang {piano_tuple[2:5]}")