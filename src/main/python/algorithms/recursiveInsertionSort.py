def recursiveSort(arr, n):
	if n > 1:
		yield from recursiveSort(arr, n-1)
		last = arr[n-1]
		j = n-2

		while(j >= 0 and arr[j]>last):
			yield arr, j ,-1, j+1, -1
			arr[j+1] = arr[j]
			j = j-1

		arr[j+1] = last

def recursiveInsertionSort(array, *args):
	n = len(array)
	yield from recursiveSort(array, n)