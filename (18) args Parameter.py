# *args = a parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments
#         the * is the most important part. We can change the name to anything

# here, the function only takes 2 arguments. What if 3 arguments are passed, the program will give error
def sum(num1, num2):
    sum = num1 + num2
    return sum

print(sum(2, 5))

# so to make the function be able to take as many values as the user want to calculate, we use *args
# here, the function takes as many arguments as user inputs and adds them all with the help of for loop
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1, 2, 595, 35))

def mul(*nums):
    product = 1
    for i in nums:
        product *= i
    return product

print(mul(2, 2, 2, 2))

# As the arguments that are passed in it becomes a tuple and tuples are immutable (unchangeable)
# so we'll typecast the tuple into a list to change a specific index's element

def sum(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 10
    for i in stuff:
        sum += i
    return sum

print(sum(5, 5))






