def fOcc(arr, low, high, x, n) : 
    if(high >= low) : 
        mid = low + (high - low) // 2
        if( ( mid == 0 or x > arr[mid - 1]) and arr[mid] == x) : 
            return mid 
        elif(x > arr[mid]) : 
            return fOcc(arr, (mid + 1), high, x, n) 
        else : 
            return fOcc(arr, low, (mid - 1), x, n) 
      
    return -1
  
  
 
def lOcc(arr, low, high, x, n) : 
    if (high >= low) : 
        mid = low + (high - low) // 2
        if (( mid == n - 1 or x < arr[mid + 1]) and arr[mid] == x) : 
            return mid 
        elif (x < arr[mid]) : 
            return lOcc(arr, low, (mid - 1), x, n) 
        else : 
            return lOcc(arr, (mid + 1), high, x, n) 
              
    return -1     
  

arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
n = len(arr)   
x=8
l1=fOcc(arr, 0, n - 1, x, n)
l2=lOcc(arr, 0, n - 1, x, n)
print("First Occurrence = ",       fOcc(arr, 0, n - 1, x, n)) 
print("Last Occurrence = ",       lOcc(arr, 0, n - 1, x, n)) 
print("Count = ",l2-l1+1)