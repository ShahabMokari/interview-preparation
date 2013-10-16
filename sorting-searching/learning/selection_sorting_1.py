def selectionSort(A):
	counter = 0
	for i in range(len(A)-1):
		min = i
		for j in range(i,len(A)):
			if A[min] > A[j]:
				min = j
			counter += 1
		A[i], A[min] = A[min], A[i]
	return A, counter
if __name__ == '__main__':
	n = [3, 53, 9, 2, 5]
	print selectionSort(n)
