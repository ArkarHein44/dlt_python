# star triangle print 
def triangle_star(stars):
	for i in range(1,stars+1):
		for k in range(i):
			print("*", end="")
		print("")
	
triangle_star(3)