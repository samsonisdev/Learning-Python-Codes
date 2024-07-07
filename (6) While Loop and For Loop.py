# while loop: a statement that will execute a block of code as log as it's condition remains true
import time

name = ""

while len(name) == 0: # if length of name is 0(means no name entered) the loop will continue asking to enter name
    name = input("Enter your name: ")

print("Hello " + name)

name = None # another example
while not name:
    name = input("Enter your name: ")

print("Hello " + name)
## -----------------------------------------------------------------------------------------
## for loop: a loop that will execute a block of code a limited amount of times
##                  while loop = unlimited
##                  for loop = limited

for i in range(10): # i stands for index
    print(i)

for i in range(10): # as this will print till 9, we can add +1 in range(10+1) or in print(i+1)
    print(i+1)

for i in range(50, 100+1, 2): # here, (starting point, ending point, step)
    print(i)

for i in "Samson": # prints each letter line by line
    print(i)

for i in range(1, 11):
    print("2 x ", i, "=", 2*i)

number = int(input("Enter number of table: "))

for i in range(1, 11):
    print(number, " x ", i, " = ", number*i)


# ------------------------------------------------------------------------------------------
# Here we're gonna print a count down from 10 to 0, and it'll print HAPPY NEW YEAR!!!
for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1) # means that it'll print the numbers after 1 second like a count down
for wish in "TADOW!", "Happy New Year", "Hope this year is blessed for you!!":
    print(wish)
    time.sleep(1)
print("HAPPY NEW YEAR!!")

for love in "I LOVE U":
    print(love)
    time.sleep(1)