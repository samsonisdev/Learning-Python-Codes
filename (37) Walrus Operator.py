# Walrus Operator  :=

# new to Python 3.12
# assignment expression also known as walrus operator
# assigns values to variables as part of a larger expression

# for example:
happy = True
print(happy)

# by using walrus operator
print(happy := True)

# another example:
# foods = list()
# while True:
#     food = input("What foods do you like?: ")
#     if food == 'quit':
#         break
#     foods.append(food)

# by using walrus operator
foods = list()
while food := input("What foods do you like?:") != 'quit':
    foods.append(food)