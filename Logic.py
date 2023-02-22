import os # os is auto included with python. Other modules will not be
os.system('clear') # use whatever command is needed for that instance; gitbash uses "clear"

## Assingment Operators

# "=" Basic assignment
# "+, -, *, /, **, % ="" Do the math operator to the variable with and assign it back to the variable
# num += 1 adds 1 to nums and reassigns to nums
# num *=2 multiplies nums by 2 and reassigns to nums


## Comparison Operators
# == "equals"
# != "Not Equal"
# > "Greater Than"
# < "Less Than"
# >= "Greater Than or Equal to"
# <= "Less than or Equal to"
# Results in a boolean
# Can compare strings as well (case senstive)
# Can compare lists as well

print(10 == 10) # Prints "True"
print("John" < "Test") # True
print("John" > "Test") # False, so clearly some level of encoding
# From Stack overflow on comparing strings
'''
The first bytes are compared and if the ordinal value of the first is less than of the second, it's lesser. 
If it's more, it's greater. If they are the same, the next byte is tried. 
If it's all ties and one is longer, the shorter one is lesser.

Lexicographical ordering for strings uses the ASCII ordering for individual characters
'''

# Lists follow the same idea
print([1,2] > [2,3])
print([1,2] < [1,3])


## Conditional Statements
# if / else / elif
# Python uses indenting to determine where the if statement starts and ends
num = 15

''' Basic If Statement
if (num > 10):
    print(num, " is greater than 10")
    #print("%(num)d is greater than 10" % {"num": num})
elif(num == 10)
    print("Your number is 10")
else:
    print(num, " is less than 10")
'''

## Multiple Conditions
# Use Parentheses to group as needed
# not() is negation
if (num > 10) and (num >100):
    print(num, "is greater than 10 and 100")

if (num > 10) or (num > 100):
    print(num, "is greater than 10 or greater than 100")