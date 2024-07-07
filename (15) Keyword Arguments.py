# Keyword Arguments = arguments preceded by an identifier when we pass them to a function
#                     The order of the arguments doesn't matter, unlike positional arguments
#                     Python knows the names of the arguments that our function receives

# this is how we use positional arguments (the common one)
def name(first, middle, last):
    print("Hello", first, middle, last)

name("Samson", "DUDE", "Rizz")

# this is how we use keyword arguments
def name(first, middle, last):
    print("Hello", first, middle, last)

name(last="Rizz", middle="dude", first="Samson")