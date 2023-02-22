import os # os is auto included with python. Other modules will not be
os.system('clear') # use whatever command is needed for that instance; gitbash uses "clear"

## While Loop
# as with if, uses indents to determine nesting

counter = 0
while (counter < 10):
    counter+=1
    print(counter)


## For Loop

# With Strings
name = "Benjamin"
for n in name:
    print(n) # n is the value, not the index
    # print auto starts a new line at the end

# With Lists; exactly as expected
testList = [5, 10, 20, 30, [61,62,63]]
for n in testList:
    print(n) 

# With Dictionaries, take both key and value as input and can reference either
favPizza = {
    "John" : "Pepperoni",
    "Tim" : "Mushroom",
    "Mary" : "Cheese",
}
for key,value in favPizza.items():
    print(key, " likes ", value, " pizza.") 
