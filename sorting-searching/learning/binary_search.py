def bs(A, a):
	if len(A) < 1:
		print "list is empty"
		return 
	elif A[0] <= a and A[-1] <= a:
		mid = len(A)//2
		print mid

		if A[mid] == a:
			print A[mid]
		elif A[mid] > a:
			bs(A[:mid], a)
		elif A[mid] < a:
			bs(A[mid:], a)


	
