# making a super class of mammals and two subclasses of dog and cat and at least 6 objects for each class 
class mammals:
    def __init__(self, legs, teeth):
        self.legs = legs
        self.teeth = teeth

    def speak(self):
        return f"A mammal with {self.legs} legs and {self.teeth} teeth ."

class dog(mammals):
    def __init__(self, size, breed, legs, teeth):
        super().__init__(legs, teeth)
        self.size = size
        self.breed = breed

    def speak(self):
        return f"A {self.size} dog of breed {self.breed} barks: Woof! and has {self.legs} legs and {self.teeth} teeth."

class cat(mammals):
    def __init__(self, size, color, legs, teeth):
        super().__init__(legs, teeth)
        self.size = size
        self.color = color

    def speak(self):
        return f"A {self.size} cat with {self.color} fur meows: Meow! and has {self.legs} legs and {self.teeth} teeth."

# Create instances of each class
dog1 = dog("Large", "Golden Retriever", legs=4, teeth=32)
dog2 = dog("Medium", "German Shepherd" , legs=4, teeth=42)
dog3 = dog("Small", "Bulldog" , legs=4, teeth=40)

cat1 = cat("Large", "Orange" , legs=4, teeth=26)
cat2 = cat("Medium", "Gray" , legs=4, teeth=34)
cat3 = cat("Small", "Black" , legs=4, teeth=30)

# Test the speak method for each object
print(dog1.speak())  
print(dog2.speak())  
print(dog3.speak())  

print(cat1.speak())  
print(cat2.speak())  
print(cat3.speak())  