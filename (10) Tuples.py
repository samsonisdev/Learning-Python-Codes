# Tuples =  a collection that is ordered and unchangeable
#           used to group together related data

student = ("Samson", 18, "male")

print(student)
print(student.index(18)) # finding on which index the entered element is
print(student.count("male"))

for x in student:
    print(x)

if "Samson" in student:
    print("Samson is here!")

list = [4, 5, 6, 'shamoon']
list[1] = 'sohaib'

print(list)


