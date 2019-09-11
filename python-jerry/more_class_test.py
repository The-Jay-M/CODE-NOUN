#__init__ method is called class constructor
class Student:
    def __init__(soul, name, first, second, third, fourth):
        soul.name = name
        soul.first = first
        soul.second = second
        soul.third = third
        soul.fourth = fourth
test= Student("Bob", 10, 20, 30, 40)
print(test.third)

#classes can have other methods defined to add functionality
class Dog:
    def __init__(initial, name, color):
        initial.name = name
        initial.color = color

    def bark(initial):
        print("woof!")

fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()

floyd = Dog("Floyd", "white")
print(fido.name)
floyd.bark()
