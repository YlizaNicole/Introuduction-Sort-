import colorama
from colorama import Fore

def bubbleSort(arr):
    n = len(arr)
    swapped = False

    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            return
 
 
arr = [83, 86, 41, 29, 43, 58, 76, 77, 52,15]
n = len(arr)
print(Fore.RED + "unsorted")
for i in range(n):
    print("%d" % arr[i],end=" ")

 
bubbleSort(arr)
print("")
print(Fore.GREEN + "sorted",)
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")