# High Order Functions = a function that either:
#                        1. accepts a function as an argument
#                        OR
#                        2. returns a function
#                        (In python, functions are also treated as objects)

# 1. Accepting a function as an argument:
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("I'm Shamoon")
    print(text)

hello(loud)

# Returns a function:
def divisor(x):
    def divident(y):
        return y / x
    return divident

divide = divisor(2)
print(divide(10))
