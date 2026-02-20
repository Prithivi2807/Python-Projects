# List of lines to write to the file
Lines = ["This is line 1", "This is line 2", "This is line 3"]

# Create a new file Example3.txt for writing
with open('Example3.txt', 'w') as file2:
    for line in Lines:
        file2.write(line + "\n")
    # file2 is automatically closed when the 'with' block exits