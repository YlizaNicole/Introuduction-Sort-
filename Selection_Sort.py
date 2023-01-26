import colorama
from colorama import Fore

def selectionSort(array, size):
    
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):

            if array[j] < array[min_index]:
                min_index = j

        (array[ind], array[min_index]) = (array[min_index], array[ind])
 
arr = [83, 86, 41, 29, 43, 58, 76, 77, 52, 15]
n = len(arr)
print(Fore.RED +"Unsorted")
for i in range(n):
    print("%d" % arr[i],end=" ")
selectionSort(arr, n)
print("")
print(Fore.GREEN +"sorted")
for i in range(n):
    print("%d" % arr[i],end=" ")