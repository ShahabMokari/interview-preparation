def quickSort(A, start, end):
	"""
	Quick sort demo.
	"""

	if isinstance(A, list) != True:
		print "pls enter a list"
		return
	if start > end:
		return
	n = len(A)
	if n <= 1:
		return A

	s = partition(A, start, end)
	quickSort(A, start, s-1)
	quickSort(A, s+1, end)
	return A

def partition(A, l, r):
	p = A[l]
	i = l+1
	j = r

	while i <= j:
		while i <= j and A[i] < p:
			i += 1
		while i <= j and A[j] > p:
			j -= 1

		if i <= j:
			A[i], A[j] = A[j], A[i]
			i, j = i+1, j-1
	A[l], A[j] = A[j], A[l]
	return j

