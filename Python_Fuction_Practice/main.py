
# Create function to determine if water is boiling AFTER converting to C
def temp (x):
    if (x < 100):
        print('Not Boiling')
    elif (100 <= x < 374):
        print('Boiling')
    elif (x >= 374):
        print('Supercritical')

# Create function to convert water temp from F to C
def convert (x):
    y = (x - 32) * 5 / 9
    print(y)
    temp(y)

# Prompt user to input temp
temp_input = float(input('Please enter a temperature in F: '))

# Call convert function
convert(temp_input)








