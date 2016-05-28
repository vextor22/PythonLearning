def Main():
	words = ["cat","sat","bat", "map"]
	with open("words.txt", "w") as f:
		for word in words:
			f.write(word + '\n')
	
if __name__ == "__main__":
	Main()