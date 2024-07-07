# slicing: create a substring by extracting elements from another string
#           indexing[]         or   slice()
#           [start:stop:step]       (start,stop,step)

# name = "Samson Rizz"
# first_name = print(name[0:6])
# last_name = print(name[7:11])
# funky_name = print(name[0:11:2]) # this means, print only characters leaving one after another

name = "Samson Rizz"
first_name = print(name[:6]) # if we don't add a starting point, python will assume it's index is 0
last_name = print(name[7:]) # if we don't add a stopping point, python will assume it's going till the end
funky_name = print(name[::2]) # if we don't add starting or stopping point, python will assume it's starting from 0 till the end
reversed_name = print(name[::-1])

website1 = "http://google.com"
website2 = "http://wikipedia.com"
slice = slice(7, -4) # slices the part till index 7 and till -4 (from right side)

print(website1[slice])
print(website2[slice])
