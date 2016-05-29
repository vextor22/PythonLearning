class MyClass:
	number = 0
	name = "noname"
	
def Main():
	me = MyClass()
	
	me.number = 1337
	me.name = "Matt"
	
	notMe = MyClass()
	
	print(me.name + " " + str(me.number))
	print(notMe.name + " " + str(notMe.number))
	
if __name__ == "__main__":
	Main()