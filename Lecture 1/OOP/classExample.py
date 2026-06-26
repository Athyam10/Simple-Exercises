class Person:

   #  def __init__(self):          # Constructor
   #     self.name = "Hasan"
   #     self.age = 60

   def __init__(self,name,age,gender):          # Constructor
    self.name = name
    self.age = age
    self.gender = gender

    def __str__(self):
         return "Name: {}, Age: {}, Gender: {}".format(self.name,self.age,self.gender)
    

# Object creation (instantiation of a class)
aPerson = Person("Hasan", 60, "M")
print("Printing uniques identfier of the object: **************************************")
print(aPerson)

print("Printing all properties of the object one at a time :**************************************")
print(aPerson.name)
print(aPerson.age)
print(aPerson.gender)

anotherPerson = Person("Jane", 50, "F")
print(anotherPerson.age) 
print(anotherPerson.gender) 
print(anotherPerson.name) 


