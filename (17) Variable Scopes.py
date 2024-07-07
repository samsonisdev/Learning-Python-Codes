# scope = The region that a variable is recognized
#         A variable is only recognized from the region it is created
#         A global and locally scoped versions of a variable can be created

name = "Rizz" # global scope / variable (available inside and outside functions)

# def my_name():
#     name = "samson" # local scope / variable (available only inside this function) we can't access this variable outside of this function
#     print(name)
#
# my_name()
# print(name)

# if we don't have a local variable inside the function, the global variable will print if it's available
name = "Rizz"

def my_name():
    #name = "samson"
    print(name)

my_name()
