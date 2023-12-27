# Hi Hannah
def hannahs_awesome_function (x): # Determine if hannah can pick the right number
    while not x == 0:
        if x == 27:
            print("It's already been a month!!")
        elif x == 69:
            print('Nice!')
        elif x == 9:
            print('Ya Boi!')
        elif x != 27 or x != 69 or x != 9:
            print('Choose another number dweeb!')
        x = float(input('Please pick a number (0 to exit): '))

    print('Have a great day Hannah!')
def hannahs_awesome_function2 (): # Create input for Hannah's function
    y = float(input('Please pick a number (0 to exit): '))
    hannahs_awesome_function(y)

hannahs_awesome_function2() # Call da function
