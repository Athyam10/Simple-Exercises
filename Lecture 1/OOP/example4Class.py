class Person:
	
	def __init__(self, name,age,gender):
		self.name = name
		self.age = age
		self.gender = gender

	def __str__(self):
         return "Name: {}, Age: {}, Gender: {}".format(self.name,self.age,self.gender)
    
obj2 = Person("Jane", 50, "f") 
print(obj2)

obj1 = Person("Hasan", 60, "M")
print(obj1)

# print("Obj1 name is " + obj1.name + " and obj1 age is "+ str(obj1.age))
# print("Obj2 name is " + obj2.name + " and obj2 age is "+ str(obj2.age))

