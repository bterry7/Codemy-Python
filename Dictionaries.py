import os # os is auto included with python. Other modules will not be
os.system('clear') # use whatever command is needed for that instance; gitbash uses "clear"

# key:value
# Reference key, get value
# Can use numbers as keys. Cannot use lists
# Pretty much any variable type can be a value ... even a dictionary

favorite_pizza = {
    "John": "Pepperoni",
    "Tim": "Sausage",
    "Mary" : "Cheese"
}

print(favorite_pizza["John"])

# Delete item from Dictionary
del favorite_pizza["John"] # deletes key value pair
print(favorite_pizza)

# Add pair to Dictionary
favorite_pizza.update({"Tina":"Green Pepper"}) 
print(favorite_pizza)

# Changing value
favorite_pizza["Tim"] = "Green Pepper"
print(favorite_pizza)

test = {
    1 : [1,2,3],
    2: [4,5,6,[7,8,9]]
}
print(test)
print(test[2][3][0])

test2 = {
    1 : {"John" : 1, "Tina": 2},
    2: 2
}
print(test2[1]["John"])