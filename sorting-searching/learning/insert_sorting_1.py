def insertSort(A):
	counter = 0
	for i in range(1, len(A)):
		while i >= 1:
			if A[i] < A[i-1]:
				A[i], A[i-1] = A[i-1], A[i]
				counter += 1
				print A, counter
				i -= 1
			else:
				break
	return A

if __name__ == '__main__':
	n = [89, 45, 68, 90, 29, 34, 17]
	print insertSort(n)

