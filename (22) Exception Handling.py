# Exception = events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ValueError as e:
    print(e)
    print("You can only divide numbers!")
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero! Stupid!")
except Exception as e:
    print(e)
    print("Something went wrong!")
else:
    print(result)
finally: # this means this block will always execute no matter the above conditions meet or not
    print("This will always execute")