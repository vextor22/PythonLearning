import math

def Main():
	try:
		radius = float(input("Please enter a radius: "))
		area = math.pi * radius**2
		print("The area is:", area)
	except:
		print("You didn't enter number... naughty naughty")
		Main()
	
if __name__ == "__main__":
	Main()