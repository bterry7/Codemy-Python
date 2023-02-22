import os # os is auto included with python. Other modules will not be
os.system('clear') # use whatever command is needed for that instance; gitbash uses "clear"


# Print all numbers 1 to 100
# if divisible by 3, print fizz
# if divisible by 5, print buzz
# if divisible by both, pring FizzBuzz

num1 = 3
num2 = 5
lim = 1000
string = ""

# Extra Challenge
# Count the fizzes, buzzes and fizzbuzzes (exclusive, i.e. fizzbuzz does not count as fizz or buzz)
fizz = 0
buzz = 0
fizzbuzz = 0

for i in range(lim):
    if ((i+1)%num1==0):
        string += "Fizz"
        fizz +=1
    if ((i+1)%num2==0):
        string += "Buzz"
        buzz +=1
        if(string == "FizzBuzz"):
            buzz -=1
            fizz -=1
            fizzbuzz+=1

    print("%(num)d: " %{"num":i+1},string)
    string = ""

print('# of just \"fizz\":',fizz)
print('# of just \"buzz\":',buzz)
print('# of \"fizzbuzz\":',fizzbuzz)
# Can format to include commmas in large numbers if needed; check out later