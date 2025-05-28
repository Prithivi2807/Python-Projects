# Breaking out the statement
while True:  # while true is an infinite loop it never ends so the input keep getting
    Line = input('Enter The line of Input >>')
    if Line == ('done'):  # once the done statement is true then only it breaks the loop and the program is ended
        print('Program Ended')
        break
    print(Line)
print('program ended successfully')
