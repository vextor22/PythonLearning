def getInteger(prompt):
	result = int(input(prompt))
	return result

def Main():
	output = []
	output.append(getInteger("Please enter an integer: "))
	output.append(getInteger("got any more a them ints? "))
	output.append(getInteger("got any more a them ints? "))
	total = 0
	for num in output:
		total += num
	output.append(total)
	
	
	print(output)
	
if __name__ == "__main__":
	Main()