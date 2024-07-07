# List = used to store multiple items in a single variable

food = ["Pizza", "Hamburger", "Hotdog", "Fries", "Pudding"]

food[0] = "Sushi" # updates the element in the list
#print(food[1]) # prints the element present on the given index

food.append("Ice Cream")
# food.remove("Sushi")
# food.insert(0, "Coke")
#food.pop()
food.reverse()
food.sort()
# food.clear()

for i in food:
    print(i)

#---------------------------------------------------------------------------------------------

# 2D Lists = a list of lists

drink = ["coffee", "tea", "soda"]
dinner = ["hamburger", "pizza", "sandwich"]
dessert = ["cake", "ice cream"]

menu = [drink, dinner, dessert] # this menu is a list that has 3 lists inside it
print(menu)
print(menu[0]) # here we're accessing the list on index 0 in menu
print(menu[2][1]) # here we're accessing the list on index 2 in menu and its element on index 1

for x in menu:
    print(x)
