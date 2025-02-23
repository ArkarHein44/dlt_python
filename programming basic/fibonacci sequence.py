def find_fibonacci(time):
	f = 0
	s = 1
	
	for i in range(time):
		t = f
		f = s 
		s = t+f
		print(f"{f} ",end="")

find_fibonacci(5)  # 1 1 2 3 5 
