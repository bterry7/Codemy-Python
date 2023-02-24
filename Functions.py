import os # os is auto included with python. Other modules will not be
os.system('clear') # use whatever command is needed for that instance; gitbash uses "clear"

# import the module we made
from Modules import namer # to call by name. Otherwise use Modules.name()
namer("Ben")

# tabs for spacing
# Must be defined before use; best practice is to define all before everything else
def nameit(first_name, last_name):
    print(first_name,last_name) # space is auto included

nameit("Ben","Terry")

# Key word "return"
def mathit(num1, num2):
    return (num1+num2)

test = mathit(2,5)
print(test)