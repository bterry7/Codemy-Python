import os # os is auto included with python. Other modules will not be
os.system('clear') # use whatever command is needed for that instance; gitbash uses "clear"

# Using quotation marks in Python
# Wrap in '' and use "" or vice versa
test = 'My boss yelled "Get Back to Work"'
print(test)

# or use escape character: \
test2 = "My boss yelled \"Get Back to Work\""
print(test2)

# common escape characters are \n for new line
test3 = "My boss yelled \n\"Get Back to Work\""
print(test3)


# Concatenation: use +
# Can only add strings
name = "Ben Terry"
greeting = "Hello, my name is " + name
print(greeting)


# String Functions
# str variable.function()
# .upper() and .lower() makes all letters uppercase or lowercase, respectively
# .capitalize capitalizes first letter in string
# .title() uppercases first letter of every word
# .swapcase() switchs upper to lowercase and vice versa
# .split(character to split by) 
print(greeting.split(" ")) # produces ['Hello,', 'my', 'name', 'is', 'Ben']
print(greeting.split(" ")[4:6]) # Can index like a list


# len(str variable) returns number of characters (counting spaces, punctuation, etc.)
# can use [] just like with arrays to get a specific character in the string. Also 0 indexed
# can use : for ranges (go 1 past end index)
print(greeting[0:5])