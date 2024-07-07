# super() = Function used to give access to the methods of a parent class
#           Returns a temporary object of a parent class when used

# Here, the child classes (square class and cube class) is having length and width in common. So what we can do is, use the super function

# class Rectangle:
#     pass
#
# class Square(Rectangle):
#
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length*self.width
#
# class Cube(Rectangle):
#
#     def __init__(self, length, width, height):
#         self.length = length
#         self.width = width
#         self.height = height
#
#     def volume(self):
#         return self.length*self.width*self.height
#
#
# square = Square(3, 3)
# cube = Cube(3, 3,3)
#
# print(square.area())
# print(cube.volume())


# By using the super(), we can move the common methods of child classes in the parent class and then use the parent class method in the child classes so that it's reusable

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):

    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length*self.width

class Cube(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height

# Creating objects
square = Square(3, 3)
cube = Cube(3, 3,3)

print(square.area())
print(cube.volume())
