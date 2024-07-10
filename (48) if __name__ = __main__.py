# ------------------------------|
# if __name__ == '__main__'
# ------------------------------|

# 1. Module can be run as a standalone program
#    or
# 2. Module can be imported and used by other modules

# Python interpreter sets "special variables", one of which is __name__
# Python will assign the name variable with the value of '__main__' if it's
# the initial module being run

# if I print __name__ I get __main__ in console
print(__name__)

# For example if I make two modules named module_1 and module_2,
# and import module_2 in _module_1 and run the if/else statements below


# if we're running a module directly, see, the if condition runs, cuz we're in the same module
if __name__ == '__main__':
    print("Running this module directly")

# but if we were in a diff module, and we imported this module to any other file, the else condition would run
else:
    print("Running other module indirectly")

# it's like the __name__ variable stores the name of the module/file that we're working on
