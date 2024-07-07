# Loop Control Statements: change a loop execution from its normal sequence

# break =               used to terminate the loop entirely
# continue =            skips to the next iteration of the loop
# pass =                does nothing, acts as a placeholder

# while True:
#     name = input("Enter your name: ")
#     if name != "": # if name variable is not an empty space means if user has entered the                          name, break the loop
#         break

# ----------------------------------------------------------------------------------------------

# phone_no = input("Enter your number: ")
# for i in phone_no:
#     if i == "-": # (means if i finds "-" in phone_no, it should skip it (continue it)
#         continue
#     print(i, end="") # end="" used to print all the numbers in the same line


# phone_no = input("Enter your number: ")
# for i in phone_no:
#     if i.isdigit():
#         print(i, end="")

# --------------------------------------------------------------------------------------------

for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)