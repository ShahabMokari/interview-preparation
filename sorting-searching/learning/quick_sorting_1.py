def quickSort(Aa, l, r):
	if l > r:
		return
	s = partition(Aa, l, r)
	quickSort(Aa, l, s-1)
	quickSort(Aa, s+1, r)
	return Aa

def partition(A, h, t):
	p = A[h]
	i = h+1
	j = t
	while i <= j:
		while i <= j and A[i] < p:
			i += 1
		while i <= j and A[j] > p:
			j -= 1
		if i <= j:
			A[i], A[j] = A[j], A[i]
			i, j = i+1, j-1

	# be careful with the following code, I make mistake twice here
	A[h], A[j] = A[j], A[h]
	return j

if __name__ == '__main__':
	n = [5, 3, 1, 9, 8, 2, 4, 7]
	print quickSort(n, 0, 7)
