# thread = a flow of execution. Like a separate order of instructions.
#          However, each thread takes a turn running to achieve concurrency
#          GIL = Global Interpreter Lock
#          allows only one thread to hold the control of Python Interpreter at any one time


# cpu bound = program/task spend most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing
# io bound =  program/task spend most of it's time waiting for internal events (user input, webscraping)
#             use multithreading

# Suppose we need to download 5 files from internet.
# So logically we don't want to wait for 1 file to download and then head over
# to download other 4 files one by one. We want to download all 5 files simultaneously to save time
# That's where we use threading to do more than one tasks at once.


import threading
import time

def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

# Normal Code: (this code takes 10 seconds to complete)
# time1 = time.perf_counter() # recording the time taken by assigning the starting point
# func(4)
# func(3)
# func(2)
# func(1)
# time2 = time.perf_counter() # recording the time taken by assigning the ending point
# print(time2-time1) # calculating time

# Same code using threads: (this code takes less than 1 second to complete
time1 = time.perf_counter()
t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[3])
t3 = threading.Thread(target=func, args=[2])
t4 = threading.Thread(target=func, args=[1])

t1.start()
t2.start()
t3.start()
t4.start()

time2 = time.perf_counter()
print("\n", time2 - time1)
