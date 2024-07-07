# if statement: a block of code that wil execute only if it's condition is true

age = int(input("How old are you?: "))

if age == 100:
    print("You're a century old!")
elif age > 100:
    print("You're more than a century old!")
elif age >= 18:
    print("You're an adult!")
else:
    print("You're a child")

if 20 <= age <= 29:
    print("You're in your twenties!")
elif 30 <= age <= 39:
    print("You're in your thirties!")
elif 18 <= age <= 19:
    print("You're a teenager!")

# logical operators(and, or, not): used to check if two or more conditional statements are true

temp = int(input("What's the temperature outside today?: "))

if temp >= 0 and temp <= 30: # (and) print this statement if both of these conditions are true
    print("Temperature is good today! Go outside!")
elif temp < 0 or temp > 30: # print this statement if one of these conditions are true
    print("Temperature is bad today! Stay inside!")

if not(temp >= 0 and temp <= 30): # not logical operator flips the true to false and vice versa
    print("Temperature is good today! Go outside!")
elif not(temp < 0 or temp > 30):
    print("Temperature is bad today! Stay inside!")

