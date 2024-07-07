# str.format() = optional method that gives user more control when displaying output

animal = "cow"
item = "moon"

# this is a common way to add a variable within a string
print("The " + animal + " jumped over the " + item)

# another way using str.format(). We're using placeholders{} here.
# The curly braces are called format fields
print("The {} jumped over the {}".format(animal, item))

# another way using str.format(). We're using placeholders here with positional arguments
# we can use the same index more than once
print("The {1} jumped over the {1}".format(animal, item))

# another way using str.format(). We're using placeholders here with keyword arguments
# We don't need the variables this time that we created at the beginning
# we can use the same keyword more than once
print("The {item} jumped over the {item}".format(animal="cow", item="moon"))

# another way using str.format() by storing the string in a variable
text = "The {} jumped over the {}"
print(text.format("cow", "moon"))

# ---------------------------------------------------------------------------------------------

# HOW TO ADD A PADDING TO A TEXT
name = "Samson"

print("My name is {}".format(name)) # no padding
print("My name is {:10}. Nice to meet you!".format(name)) # padding added
print("My name is {:<10}. Nice to meet you!".format(name)) # left alignment
print("My name is {:>10}. Nice to meet you!".format(name)) # right alignment
print("My name is {:^10}. Nice to meet you!".format(name)) # center alignment

# ---------------------------------------------------------------------------------------------
# HOW TO FORMAT NUMBERS

number1 = 3.14159
number2 = 1000000
print("The number pi is {}".format(number1))
print("The number pi is {:.3f}".format(number1)) # the .f will also round off the numbers
print("The number is {:,}".format(number2)) # this will add commas where needed in a number
print("The number is {:b}".format(number2)) # b to convert to binary
print("The number is {:o}".format(number2)) # o to convert to octal
print("The number is {:x}".format(number2)) # x/X to convert to hexadecimal
print("The number is {:e}".format(number2)) # e/E to convert to scientific notation
