def mergeSort(A):
	if len(A) < 2:
		return

	A1 = A[:len(A)//2]
	A2 = A[len(A)//2:]

	mergeSort(A1)
	mergeSort(A2)
	merge(A1, A2, A)
	return A

def merge(A1, A2, A):
	i = j = 0
	while j+i < len(A):
		if i == len(A1) or j < len(A2) and A1[i] > A2[j]:
			A[i+j] = A2[j]
			j += 1
		else:
			A[i+j] = A1[i]
			i += 1

if __name__ == '__main__':
	n = [3, 53, 9, 2, 5]
	print mergeSort(n)
