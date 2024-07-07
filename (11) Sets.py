# Set = a collection of unordered and un-indexed elements. Do not print duplicate values

utensils = {"spoon", "knife", "fork", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

#print(utensils) # it'll print the elements in any order and won't print same elements

# utensils.add("napkin")
# utensils.remove("fork")
# dishes.add("mug")
# utensils.update(dishes) # adding all the elements of dishes in utensils
# dinner_table = utensils.union(dishes) # prints all the elements in both dishes and utensils
print(utensils.difference(dishes)) # it'll print what utensils has that dishes doesn't
print(dishes.difference(utensils)) # it'll print what dishes has that utensils doesn't
print(utensils.intersection(dishes)) # prints what they both have in common

# for x in dinner_table:
#     print(x)
