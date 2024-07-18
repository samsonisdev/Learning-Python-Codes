# daemon thread = a thread that runs in the background, not important for program to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non daemon threads cannot normally be killed, stay alive until task is complete
#
#                 ex. background tasks, garbage collection, waiting for input, long running process

import threading
import time

def timer():
    counter = 0
    while True:
        time.sleep(1)
        counter += 1
        print("User logged in for", counter)

x = threading.Thread(target=timer, daemon=True)
x.start()

# x.setDaemon(True/False) # used to convert a thread to daemon or non-daemon
# x.isDaemon() # used to check is a thread is daemon or not

answer = input("do you wish to exit?")

