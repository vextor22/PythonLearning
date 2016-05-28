def Main():
	try:
		f = open(input("What file would you like to open? "), "r")
		for line in f:
			print(line, end="")
	except:
		print("File was not found")
	
	
	
if __name__ == "__main__":
	Main()