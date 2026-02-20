# Data to append to the existing file
new_data = "This is line C"

# Open an existing file Example2.txt for appending
with open('example2.txt', 'a') as file1:
    file1.write(new_data + "\n")
    # file1 is automatically closed when the 'with' block exits