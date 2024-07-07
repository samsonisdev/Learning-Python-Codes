# Method Overriding = when we use the same kind of method in two classes, the one method that
#                     is closest to its self will run instead of relying on the parent class
class Animal:

     def eat(self):
         print("This animal is eating!")

class Rabbit(Animal):

    def eat(self):
        print("This animal is eating carrot")

rabbit = Rabbit()
rabbit.eat()