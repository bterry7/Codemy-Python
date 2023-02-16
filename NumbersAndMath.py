import os # os is auto included with python. Other modules will not be
os.system('clear') # use whatever command is needed for that instance; gitbash uses "clear"

# Python follows PEMDAS

num = 10
# Convert to float with float()
# Floats will print with a trailing decimal
print(float(num))

num2 = 10.75
# Convert to int with int(); always rounds down (i.e. truncates)
# Others will not; will convert to float if one of the arguments is a float
print(int(num2))


# Convert to string with str()
print(str(num))
# Convert str to num with int() (or float()). Only works with number strings (i.e. "5", "5.25"); alpha strings will throw an error (as opposed to converting to ASCII or whatever encoding)
print(int("5"))

# Division will auto convert to float since most division is floats
print(10/2)

# ** is used for exponents
print(5**3)
# % is modulus (remainder)
print(10.5*2)