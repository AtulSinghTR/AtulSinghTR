class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name} is {self.age} years old"    
        
    # Another instance method
    def speak(self, sound):
        return f"{self.name} bark like {sound}"        
        
        
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass
        
# miles = Dog("Miles", 4, "Jack Russell Terrier")
# buddy = Dog("Buddy", 9, "Dachshund")
# jack = Dog("Jack", 3, "Bulldog")

# jim = Dog("Jim", 5, "Bulldog")        
# jim.speak('woof')

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)

print(buddy.speak('woof'))
print(miles.speak())
print(miles.speak('Grrrr'))

