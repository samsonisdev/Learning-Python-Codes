# Zip Function = aggregate elements from two or more iterables (list, tuples, set, etc)
#                creates a zip object with paired elements stored in tuples for each element
#                zip(*iterables)

usernames = ['Samson', 'dude', 'rizz']
passwords = ['samson123', 'mybro', 'rizzy6']

users = zip(usernames, passwords)
for i in users:
    print(i)

