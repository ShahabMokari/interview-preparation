def sel_sort(A):
	"""
	Selection sorting demo using python.

	If non digits in the list, ascii order will be used
	"""
        if isinstance(A, list) == False:
		print 'pls enter a list'
		return
	if len(A) < 2:
		return A

	for i in range(len(A)-1):
		#set default min number
		min = i
		for j in range(i+1, len(A)):
			if A[j] < A[min]:
				min = j  # find the min item one by one
		
		#find the min item and exchange min and default one
		if min != i:
			A[min], A[i] = A[i], A[min]
	return A
