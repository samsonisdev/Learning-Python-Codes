# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away
#
# syntax = lambda parameters:expression

# simple function:
# def double(x):
#     return x * 2
#
# print(double(4))

# By using lambda function
double = lambda x: x * 2
mul = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: "hey " + first_name + " " + last_name
age_check = lambda age: True if age >= 18 else False

print(double(2))
print(mul(3, 3))
print(add(2, 2, 2))
print(full_name("Samson", "Rizz"))
print(age_check(18))
