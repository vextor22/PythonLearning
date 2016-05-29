import math

class Vector2D:
	
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def __add__(self, other):
		return Vector2D(self.x + other.x, self.y + other.y)
		
	def getLength(self):
		return math.sqrt(self.x**2 + self.y**2)
	def normalized(self):
		length = self.getLength()
		if length != 0:
			return Vector2D(self.x/length, self.y/length)
		return self
	def getAngle(self)
		return math.degrees(math.atan2(self.y,self.x))
		
def Main():
	vec = Vector2D(5,6)

	vec += vec
	print("X:", str(vec.x),"Y:",str(vec.y))
	
	
	
if __name__ == "__main__":
	Main()