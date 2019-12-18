# Numbers
# Strings
# Booleans
# ...
# Lists
# Dictionaries


class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.draw()
point1.move()

point1.x = 10
point1.y = 10
print(point1.x)

point2 = Point()
point2.y = 10


# not available, as they are new different instance
# print(point2.x)


class PointWithCtor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self):
        print(f"x : {self.x}, y: {self.y}")


pointWithCtor = PointWithCtor(100, 20)
pointWithCtor.x += 1
print(pointWithCtor.x)
pointWithCtor.print()


class Mammal:
    def walk(self):
        print("walk")


class Cat(Mammal):
    pass


class Dog(Mammal):
    def bark(self):
        print('bark')


dog = Dog()
dog.walk()
dog.bark()
