# **kwargs = a parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword arguments
#            the ** is the most important part. We can change the name to anything

# here the function would work only if 2 arguments are passed but won't work for more than 2
def hello(first, last):
    print("Hello " + first + " " + last)

hello("Samson", "Rizz")

# so to access a varying amount of keyword arguments, we use **kwargs
# here cuz we used two parameters in the print statement (first & last) with kwargs, the function won't give an error if more that 2 keyword arguments are passed
def hello(**kwargs):
    print("Hello " + kwargs['first'] + " " + kwargs['last'])

hello(first="Samson", last="Rizz", middle="dude")

# so to access a varying amount of keyword arguments, we're using **kwargs
def hello(**names):
    print("Hello", end=" ")
    for key, value in names.items():
        print(value, end=" ")

hello(title="Mr", first="Samson", last="Rizz", middle="dude")

