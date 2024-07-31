#method overriding
class Animal:
    def speak():
        return "speaking....."
    #single
class Dog(Animal):
    def speak():
        return "dog is speaking....."
class puppy(Dog):
    def speak():
        return "puppy is speaking....."
obj3=puppy
print(obj3.speak())


#
