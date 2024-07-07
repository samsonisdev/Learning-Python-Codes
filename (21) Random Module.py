import random

x = random.randint(1, 9) # generate any random integer between any two given numbers
y = random.random() # generate any random floating point number between 0-1
print(x)
print(y)

my_list = ['rock', 'paper', 'scissors']
z = random.choice(my_list) # print any of the element in the list
print(z)

game = [1, 2, 3, 4, 5, 6, "J", "Q", "K", "A"]
random.shuffle(game) # shuffle the list
print(game)
