while True:
    Line = input('Enter The input >> ')
    if Line[0] == '#':  # continue statement ends the current iteration and jumps to top of the loop
        print(
            'continue statement end the current iteration and jumps to the top of the loop #')
        continue
    if Line == 'done':
        break
    print(Line)
print('break statement successfully runs')
