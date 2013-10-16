def binarySearch(A, K):
	"""Sorted list using binary search"""
        # test if the list is empty
        if len(A) == 0:
		print 'list is empty'
		return 
	# calculate midpoint 
	mid = len(A)//2
	if mid ==0 and  K != A[mid]:
		print 'no match found'
		return

	# three way comparsion
	# key has been found
	if K == A[mid]:
		print 'find value', K
	# key is in lower subset
	elif K < A[mid]:
		binarySearch(A[:mid], K)
	else:
	# key is in upper subset
		binarySearch(A[mid:], K)

if __name__ == '__main__':
	n1= []
	n = [1, 2, 3, 4, 5, 6, 7, 8]
	print binarySearch(n, 8)
