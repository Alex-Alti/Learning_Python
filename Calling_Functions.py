# Practice accepting user inputs with functions


def pinin(): # Function to prompt user to choose pin
    pin = int(input('Please choose a pin:'))
    return pin
savepin = pinin()

def pinwhile(): # Function with while loop to prompt user for pin
    password = int(input('Please enter the pin to enter: '))  # Prompt user to input pin
    while password != savepin:  # While loop to determine flow given user input
        print('Please enter a valid pin')
        password = int(input('Please enter the pin to enter: '))

def boiling(): # Function to convert water temp and determine state
    temp = float(input('Please enter the temp in F to convert to C and determine if it is boiling(69 to exit):'))
    while not temp == 69:
        Celsius = (temp - 32) * 5 / 9  # convert temperature
        # Print converted temperature
        print(Celsius)
        # Determine if water is boiling
        if Celsius < 100:
            print('Not boiling')
        elif Celsius >= 100 and Celsius < 374:
            print('Boiling')
        elif Celsius >= 374:
            print('Supercritical')
        temp = float(input('Please enter the temp in F to convert to C and determine if it is boiling(69 to exit):'))

    print('Goodbye')

pinwhile()
boiling()






