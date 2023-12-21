# Temperature conversion and determine boiling point of water

# Prompt user for temp
Fahrenheit = float(input('Please input the temp in F to convert to C and determine if it is boiling:'))
#Convert F to C
Celsius = (Fahrenheit - 32) * 5/9
# Print converted temperature
print(Celsius)
# Determine if water is boiling
if Celsius < 100:
    print('Not boiling')
elif Celsius >= 100 and Celsius < 374:
    print('Boiling')
elif Celsius >= 374:
    print('Supercritical')



