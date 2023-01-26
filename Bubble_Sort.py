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
for i in range(n):
    print("%d" % arr[i],end=" ")

 
bubbleSort(arr)
print("Sorted array",)
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")