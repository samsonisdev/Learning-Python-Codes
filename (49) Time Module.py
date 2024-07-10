import time

print(time.ctime(0)) # convert a time expressed in seconds since epoch, to a readable string
#                      epoch = when your computer thinks time began (reference point)

print(time.time())   # return current seconds till epoch

# how to retrieve current date and time
print(time.ctime(time.time()))

#anothe way to retrieve current date and time
time_object = time.localtime() # this method will create a time object
# we'll see diff keyword arguments in output which are not readable
# so to convert them into readable form, we use:
local_time = time.strftime("%B %d %Y, %H:%M:%S", time_object)
print(local_time)

time_string = "9 July, 2024"
time_object = time.strptime(time_string, "%d %B, %Y")
# print(time_object)

# now if we give a tuple of dates or time and want that to be in a readable form...
# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = 2024, 7, 8, 5, 45, 34, 1, 6, 0
time_string = time.asctime(time_tuple)
print(time_string)

# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = 2024, 7, 8, 5, 45, 34, 1, 6, 0
time_string = time.mktime(time_tuple) # convert it to seconds till epoch
print(time_string)