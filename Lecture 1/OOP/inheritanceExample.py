# Demo of inheritance
class Person:

	def __init__(self, name, age, height):
		self.name = name
		self.height = height
		self.age = age

	def __str__(self):
		return "Name: {}, Object Age: {}, Object Height: {}".format(self.name, self.age,self.height)

	def helloWord(self):
		print("I am the objet "+ str(id(self)) + " We learn OOP, and hi to you all")

class Worker (Person):

	def __init__(self, name, age, height, salary):
		super().__init__(name,age,height)
		self.salary = salary

	def __str__(self):
		return super().__str__()+ ", Salary: {}".format(self.salary)

	def computeYearlySalary(self):
		return self.salary*12

worker1 = Worker("Hasan", 60, 176, 3000)
print(worker1)
worker1.helloWord()
print("I am making " + str(worker1.computeYearlySalary()) + " Euro in a year")


