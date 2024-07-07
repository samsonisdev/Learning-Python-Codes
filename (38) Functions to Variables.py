
def hello():
    print("Hello People!")

hello # nothing happens cuz no parentheses are added
print(hello) # I get the memory address cuz I didn't add no parentheses
hi = hello # assigning that function to a variable
hi()

# something cool:
say = print
say("Hey! how you doin")