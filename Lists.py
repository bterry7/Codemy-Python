import os # os is auto included with python. Other modules will not be
os.system('clear') # use whatever command is needed for that instance; gitbash uses "clear"

# Basic
names = ["Ben","Grace","Josh"]
print(names[0])

# Changing Items. Can also use variables
names[0] = "Ward"
print(names[0])

# Append
print(names)
name2 = "Ben"
names.append(name2)
print(names)

# Can include anything in lists; do not have to have consistent types
names.append(41)
print(names)

# ... including lists
# use [][]...[] to access lists within lists
ToAdd = ["test",1,"Bob",51]
names.append(ToAdd)
print(names)
print(names[5])
print(names[5][2])

# Use len() for total number of items. Can use to find last item
print(len(names))
print(names[len(names)-1])