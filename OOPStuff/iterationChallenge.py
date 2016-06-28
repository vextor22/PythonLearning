#------------------------//Challenge//------------------
#
#Try writing your own iterator class that allows you to specify the lengths of steps the iterator makes.
#eg.
# when you call you step iterator class you specify the steps.
#
#string = Steps('Drapsicle', 2)
#    for char in rev:
#        print(char)

#which outputs
#D,a,s,c,e

#Then try writing a generator that does the same thing!

#Hint: Learn how the range() function works!.
class Step:
	def __init__(self, data, step):
		self.data = data
		self.index = 0
		self.step = step
	def __iter__(self):
		return self
	def __next__(self):
		if(self.index >= len(self.data)):
			raise StopIteration
		nextData = self.data[self.index]
		self.index += self.step
		return nextData
		
def Main():
	rev = Step("Drapsicle", 2)
	for char in rev:
		print(char, end="")
	
if __name__ == "__main__":
	Main()