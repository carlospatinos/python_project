def fibFunction(n):
	print n
	if n<0: 
		print("Incorrect input") 
    # First Fibonacci number is 0 
	elif n==0:
		return 0 
	elif n==1: 
		return 1
    # Second Fibonacci number is 1 
	elif n==2: 
		return 1
	else:  
		return (fibFunction(n-1)+fibFunction(n-2))