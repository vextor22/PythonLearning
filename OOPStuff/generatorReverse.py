def Reverse(data):
	for index in range(len(data) - 1, -1, -1):
		yield data[index]
		
def Main():
	rev = Reverse("The work of satan")
	for char in rev:
		print(char, end="")
		
	data = "The work of satan"
	print(list(data[i] for i in range(len(data)-1, -1, -1)))
	
if __name__ == "__main__":
	Main()