def mergeSort(A):
	"""
	Merge sort demo
	"""

	if isinstance(A, list) != True:
		print "pls enter a list"
		return

	n = len(A)

	if n <= 1:
		return A

	A1 = A[:n//2]
	A2 = A[n//2:]
	
	# Using recursive way to divide the numbers
	mergeSort(A1)
	mergeSort(A2)

	# merge and sort the divided numbers
	merge(A1, A2, A)
	return A

def merge(A1, A2, A):
	"""
	Merge method to sort and merge the divided numbers.
	"""

	i = j = 0
	while i+j < len(A):
		if i == len(A1) or (j < len(A2) and A2[j] < A1[i]):
			A[i+j] = A2[j]
			j = j + 1
		else:
			A[i+j] = A1[i]
			i = i + 1

if __name__ == "__main__":
	print 'Empty list', mergeSort([])
	print 'one item list', mergeSort([1])
	print 'a string', mergeSort('This is a string')
	print 'a list with more than one item', mergeSort([2, 5, 8, 3, 7, 4, 1])

