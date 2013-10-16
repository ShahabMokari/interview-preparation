def mergeSort(A):
	"""
	Merge sort demo using python.
	"""

	if isinstance(A, list) != True:
		print "pls enter a list"
		return
	n = len(A)
	if n <= 1:
		return A
	
	A1 = A[:n//2]
	A2 = A[n//2:]
	
	mergeSort(A1)
	mergeSort(A2)
	merge(A1, A2, A)
	
	return A

def merge(Aa, Ab, Aab):
	i = j = 0
	while i+j < len(Aab):
		if i == len(Aa) or (j < len(Ab) and Ab[j] < Aa[i]):
			Aab[i+j] = Ab[j]
			j = j + 1
		else: 
			Aab[i+j] = Aa[i]
			i = i + 1
