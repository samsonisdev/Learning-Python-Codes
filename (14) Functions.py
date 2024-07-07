# # function = a block of code that is executed only when it is called. (calling a function is also called invoking a function)
#
# def hello():
#     print("Hello!!")
#     print("Have a nice day!")
#
# hello()
# hello()
# hello()
#
# #------------------------------------------------------------------------------------------------
#
# # There are parameters and arguments in a function
# def hello(name): # here, the 'name' is a parameter which works as a variable
#     print("Hello! " + name)
#
# hello("Samson") # here, 'Samson' is an argument which is stored in the parameter(name)
#
# #------------------------------------------------------------------------------------------------
#
# # We can add more than one parameter and can pass more than one argument too
# def hello(first_name, last_name):
#     print("Hello", first_name, last_name)
#
# hello("Samson", "Rizz")
#
# #------------------------------------------------------------------------------------------------
#
# # taking 3 parameters this time
# def hello(first_name, last_name, age):
#     print("Hello", first_name, last_name)
#     print("You are " + str(age) + " years old")
#
# hello("Samson", "Rizz", 18)

# ---------------------------------------------------------------------------------------------------
# Return Statement = Functions send Python values/objects back to the caller
#                    These value/objects are known as the function's return value

def multiply(number1, number2):
    result = number1 * number2
    return result

print(multiply(4, 6))

def sum(num1, num2):
    return num1 + num2

print(sum(58, 64))

