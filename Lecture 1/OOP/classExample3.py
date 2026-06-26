class Person:

   def __init__(self,name,age, gender="F"):          # 3-argument Constructor
    self.name = name
    self.age = age
    self.gender = gender

# Object creation (instantiation of a class) using 2-argument constructer
aPerson = Person("Hasan", 60)
Person.gender = "M"
print(aPerson.name)
print(aPerson.age)
print(aPerson.gender)

# Object creation (instantiation of a class) using 3-argument constructer
person2 = Person("Jane", 46,"F")
print("For the second object:")
print(person2.name)
print(person2.age)
print(person2.gender)


