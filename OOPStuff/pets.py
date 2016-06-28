class Pet:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def talk(self):
		raise NotImplementedError("Subclass must implement abstract")
		
class Cat(Pet):
	def __init__(self, name, age):
		super().__init__(name, age)
	def talk(self):
		print("meow")
		
		
class Dog(Pet):
	def __init__(self, name, age):
		super().__init__(name, age)
	def talk(self):
		print("bark")
		
def Main():
	thePet = Dog("Pet", 1)
	theCat = Cat("Jess", 4)
	
	print("is jess a Cat?", str(isinstance(theCat, Cat))) 
	print("is jess a Pet?", str(isinstance(theCat, Pet))) 
	print("is thePet a Pet?", str(isinstance(thePet, Pet))) 
	print("is thePet a Cat?", str(isinstance(thePet, Cat))) 
	
	thePet.talk()
	theCat.talk()
	
if __name__ == "__main__":
	Main()