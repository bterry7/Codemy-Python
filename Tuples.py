import os # os is auto included with python. Other modules will not be
os.system('clear') # use whatever command is needed for that instance; gitbash uses "clear"

# Tuples are lists you cannot change ... kind of
# so all of the things from lists apply, except how to change them

tuple1 = ("John","Bob","Tina")
print(tuple1)

# Artificially adding to tuples
tuple2 = ("Mary",) # have the comma at the end even for 1 item (otherwise it treats as a string, not a tuple. Lists do not have this requirement)
tuple3 = tuple1 + tuple2
print(tuple3)

# Or Artificailly remove
tuple4 = tuple1[0:2] # range is up to but not including
print(tuple4)

# So chaning tuples is basically just making new tuples by indexing or combining existing tuples
# For most applications, just use a list. Tuples are technically faster, but irrelevantly slow for most applications