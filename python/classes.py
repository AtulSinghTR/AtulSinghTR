class Dog :
    
    # Class Attribute
    species = "Canis familiaris"
    
    def __init__(self, name, age, coat_color):
        # instance Attribute
        self.name=name
        self.age=age
        self.coat_color=coat_color

    def __str__(self):
        # altering default __str__ method which returns memory location
        return f"{self.name} is {self.age} years old and belongs to {self.species} species"
        
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
    
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


dg1 = Dog('one', 5, 'brown')
dg2 = Dog('two', 8, 'golden')
philo = Dog("Philo", 5, "brown")

print("Dog1: ",dg1)
print("Dog1: ",dg2)
print(f"{philo.name}'s coat is {philo.coat_color}.")


if dg1 == dg2:
    print("Both Dog are same")
else:
    print("No, Dogs are not same")
    
print(f"Dog1 name is \"{dg1.name}\" and his age is {dg1.age} and belongs to {dg1.species} species")
print(f"Dog1 Description: {dg1.description()}")
print(f'Dog {dg1.speak("Bow")}')

if dg1.species == dg2.species:
    print("Dog's species are same")
else:
    print("No, Dog's species are not same")
    
#=====================================================

class Car:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
        
    def __repr__(self):
        return f'The {self.color} car has {self.mileage:,} miles'
    
    def drive(self, no):
        self.mileage = self.mileage + no
        

blue = Car('blue', 20000)
red = Car('red', 30000)

print(blue)
print(red)

green = Car('green', 0)
print(green)
green.drive(100)
print(green.mileage)

