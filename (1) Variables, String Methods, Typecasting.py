# variable = a container for a value. Behaves as the value that it contains

# string (a series of characters)
first_name = "Samson"
last_name = "Rizz"
full_name = first_name + " " + last_name
print("Hello " + full_name)
print(type(full_name))

# integer (a whole number)
age = 18
age += 3
print("My age is: " + str(age))
print(type(age))

# floating point (a numeric value with a decimal)
height = 5.9
print("My height is: " + str(height))
print(type(height))

# Boolean value (only stores True or False. Very useful in if else statements)
human = True
print("Are you a human: " + str(human))
print(type(human))

# multiple assignments = allows us to assign multiple variables in the same line of code
name, age, attractive = "Samson", 18, True
print(name, age, attractive)

# if different variables are supposed to have same value, we do this
Spongebob = Patrick = Sandy = 30
print(Spongebob)
print(Patrick)
print(Sandy)

# different string methods:
name = "samson"
age = "18"
print(name)
print(len(name))
print(name.find("s"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(age.isdigit())
print(name.isalpha())
print(name.count("s"))
print(name.replace("s", "k"))
print(name * 3)

# typecasting = converting variables into a different data type
a = 1
b = 2.0
c = "3"

a = float(a)
print(a)
b = print(int(b))

