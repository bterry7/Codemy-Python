# Generic Comment to practice git commits

import os # os is auto included with python. Other modules will not be
os.system('clear') # use whatever command is needed for that instance; gitbash uses "clear"


# This is a comment
'''
This is a block comment

Data Types:
Strings: text; can use "" or '' with little difference
Numbers
Lists: i.e. array; data types within do not have to be consistent. Can be nested. [] indexing, 0 indexed
Tuples: a list you can't change; makes it a little faster. Emphasis for little for most applications. Use () instead of []; rest is the same
Dictionaries: key value pairs seperated by; key and value seperated by :, each pair is seperated by a ,. Initialized using {} and are often multi-line
    Call the key in [] and the value is returned
Boolean
'''

# Variables are case sensitive
full_name = "Benjamin Terry" 
age = 27
names = ["Ben","John","Bob",41]
names_tuple = ("Ben","John","Bob")
fav_pizza = {
    "John" : "Pepperoni",
    "Bob" : "Mushroom",
    "Mary" : "Cheese"
}
test = True

print(full_name)
print(age)
print(names[1])
print(names) # printed as written code, i.e. ['item 1', item 2'], with "" if strings
print(names_tuple[0])
print(names_tuple)
print(fav_pizza["John"])
print(test)
