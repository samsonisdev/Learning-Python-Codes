# sort() method     = used with lists
# sorted() function = used with iterables/tuples

# LEVEL 1:

# For lists, we use sort() method
# we can also use sort(reverse=True) to reverse a list alphabetically
# students = ["Squidward", "Spongebob", "Sandy", "Patrick", "Mr. Krabs"]
#
# students.sort()
#
# for i in students:
#     print(i)

# For tuples, we use sorted() function
# students = ("Squidward", "Spongebob", "Sandy", "Patrick", "Mr. Krabs")
#
# sorted_students = sorted(students)
#
# for i in sorted_students:
#     print(i)

# LEVEL 2:

students_info = [("Sandy", "B", 30),
                 ("Mr.Krabs", "A", 20),
                 ("Patrick", "D", 60),
                 ("SpongeBob", "C", 25),
                 ("Squidward", "E", 79),]

grade = lambda grades:grades[1]
marks = lambda mark:mark[2]
students_info.sort(key=marks)
students_info.sort(key=grade)

for i in students_info:
    print(i)

# if students_info is a tuple of tuples, we'll use sorted() function, not sort() method
# sorted_students = sorted(students_info, key=grade)
