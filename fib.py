def fib(order):
	fibs = []
	fibs.append(0)
	if(order == 1):
		return fibs
	fibs.append(1)
	if(order == 2):
		return fibs
	for i in range(2,order):
		fibs.append(fibs[i-2] + fibs[i-1])
	return fibs
	
def recFib(order, fibs):
	if order == 0:
		return fibs
	if len(fibs) == 0:
		fibs.append(0)
		return recFib(order -1, fibs)
	if len(fibs) == 1:
		fibs.append(1)
		return recFib(order -1, fibs)
	fibs.append(fibs[len(fibs) - 2] + fibs[len(fibs) -1])
	return recFib(order - 1, fibs)

def Main():
	howMany = int(input("how many fibs to do? "))
	print(fib(howMany))
	
	fibList = []
	
	recFib(howMany, fibList)
	
	print(fibList)
	
	
if __name__ == "__main__":
	Main()