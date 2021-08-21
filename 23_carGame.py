# Build a program where there are four commands help (list of all other commands and their function)
# start prints Car Started
# stop prints Car Stopped
# exit stops the program

isStarted = False

while True:
    cmd = input('> ')
    if cmd.lower() == 'help':
        print('''start - to start the car
stop - to stop the car
quit - to exit
        ''')
    elif cmd.lower() == 'start':
        if not isStarted:
            print('Car Started...Ready to Go')
        else:
            print('Car is Already Started!!!')
        isStarted = True
    elif cmd.lower() == 'stop':
        if isStarted:
            print('Car Stopped')
        else:
            print('Car is Not Started!!')
        isStarted = False
    elif cmd.lower() == 'quit':
        break
    else:
        print("I don't Understand that")