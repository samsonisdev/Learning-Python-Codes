# Inheritance = means child class having access to all the attributes or methods found in the
#               parent class. So we don't need to write the code again n again

class Animal:  # this is the parent class

    alive = True

    def eat(self):
        print("This animal is eating!")

    def sleep(self):
        print("This animal is sleeping!")


# And these are the child classes cuz we used the parent class (Animal) after class name
# Now all these child classes will inherit everything in the parent class but these child classes can have their own unique attributes and methods too
class Rabbit(Animal):
    def run(self):
        print("This rabbit can run")


class Fish(Animal):

    def swim(self):
        print("This fish can swim")


class Hawk(Animal):

    def fly(self):
        print("This hawk can fly")

# Creating objects
rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

rabbit.run()
fish.swim()
hawk.fly()

rabbit.eat()
fish.sleep()
print(hawk.alive)