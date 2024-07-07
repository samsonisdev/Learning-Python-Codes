# list comprehension = a way to create a new list with less syntax
#                      can mimic certain lambda functions, easier to read
#                      list = [expression for item in iterable]
#                      list = [expression for item in iterable if condition]
#                      list = [expression if/else for item in iterable]
#                   e.g = [i * i       for   i    in  range(1, 11)]
#                         [expression  for  item  in  iterable]

# this program print squares of numbers in range(1, 11)
squares = []
for i in range(1, 11):
    squares.append(i*i)
print(squares)

# to do the same thing but with less syntax, we use list comprehension
squares = [i * i for i in range(1, 11)]
print(squares)

# now filtering the passed students
students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
passed_students = list(filter(lambda x: x >= 60, students))
print(passed_students)

# doing the same thing but with list comprehension (if condition)
passed_students = [i for i in students if i >= 60]
print(passed_students)

# doing the same thing but with list comprehension (if/else condition)
passed_students = [i if i >= 60 else "FAILED" for i in students]
print(passed_students)
