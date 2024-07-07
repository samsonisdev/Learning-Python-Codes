# module = a module is a file containing python code. It may contain functions, classes, etc
# used with modular programming, which is to separate a program into parts

# In this program, we're importing the module name (the file we created 'messages') and then calling the functions from that module

import messages

messages.hello()
messages.bye()

# we can also give the module a nickname, so it's easy to call

import messages as msg

msg.hello()
msg.bye()

# we can also call the functions in the same line when we're importing the module. Then we don't need to call the module name. Just need to call the functions

from messages import hello, bye

hello()
bye()

# we can also use * to have access to all the functions/classes in a module but that's dangerous
# Like this: from messages import *

# to look at the name of the modules that python has, we do this

help("modules")