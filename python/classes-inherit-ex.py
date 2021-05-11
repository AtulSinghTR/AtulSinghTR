class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
class GoldenRetriever(Dog):
    def speak(self, sound='Bark'):
        return super().speak(sound)
    
gr = GoldenRetriever('puppy', 9)
print(gr)
print(gr.speak())
print(gr.speak('Woof'))

#----------------------------------------------------------------

class Rectangle:
    
    def __init__(self,length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
class square(Rectangle):
    
    def __init__(self,side_length):
        self.length = side_length
        self.width = side_length
        
sq1 = square(5)
print(sq1.area())
    