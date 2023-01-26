import colorama
from colorama import Fore


def partition(array, low, high):

	pivot = array[high]

	i = low - 1

	for j in range(low, high):
		if array[j] <= pivot:

			i = i + 1

			(array[i], array[j]) = (array[j], array[i])

	(array[i + 1], array[high]) = (array[high], array[i + 1])

	return i + 1

def quickSort(array, low, high):
	if low < high:
		pi = partition(array, low, high)

		quickSort(array, low, pi - 1)

		quickSort(array, pi + 1, high)


arr = [83, 86, 41, 29, 43, 58, 76, 77, 52, 15]
n = len(arr)
print(Fore.RED +"Unsorted Array")
for i in range(n):
    print("%d" % arr[i],end=" ")


quickSort(arr, 0, n - 1)
print("")
print(Fore.GREEN + "Sorted")
for i in range(n):
    print("%d" % arr[i],end=" ")
