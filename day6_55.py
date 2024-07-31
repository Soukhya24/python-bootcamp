#single inheritance
class Animal:
    def speak():
        return "animal is speaking"
    #single
class Dog(Animal):
    def Bark():
        return "bow"
class puppy(Dog):
    def puppy_speak():
        return "is puppy"
obj1=Animal
obj2=Dog
obj3=puppy
print(obj3.speak())
print(obj3.Bark())
print(obj3.puppy_speak())