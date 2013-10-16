def shellSort(A):
	sublistlen = len(A)//2

	while sublistlen > 0:
		for i in range(sublistlen):
			gapInsertSort(A, i, sublistlen)
		print 'gap is ', sublistlen, A
		sublistlen = sublistlen // 2

def gapInsertSort(A, start, gap):
	for i in range(start+gap, len(A), gap):
		currentValue = A[i]
		position = i

		while position >= gap and A[position-gap] > currentValue:
			A[position], A[position-gap] = A[position-gap], A[position]
			position = position - gap

		A[position] = currentValue

if __name__ == '__main__':
	n = [5, 3, 1, 9, 8, 2, 4, 7] 
	print shellSort(n)

