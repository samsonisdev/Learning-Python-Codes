# Nested Function Calls = function calls inside other function calls
#                         innermost calls are resolved first
#                         returned value is used as an argument

# num = input("Enter a whole number = ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

# to do this all above code in a single line, we use nested function calls
num = input("Enter a whole number: ")
print(round(abs(float(num))))