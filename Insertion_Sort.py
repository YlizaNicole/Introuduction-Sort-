#Insertion Sort

def Sort(arr):
     
    if (n := len(arr)) <= 1:
      return
    for i in range(1, n):
         
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
 
arr = [83, 86, 41, 29, 43, 58, 76, 77, 52, 15]
print("unsorted array", arr)
Sort(arr)
print("")
print(arr)