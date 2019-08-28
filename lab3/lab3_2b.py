global_count=0
def bubbleSort(arr):
    n = len(arr)
    count = 0
 
    for i in range(n): 
        for j in range(0, n-i-1):
            count+=1
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return count
def selectionSort(A):
    count=0
    for i in range(len(A)): 
        
        min_idx = i 
        for j in range(i+1, len(A)): 
            count+=1
            if A[min_idx] > A[j]: 
                min_idx = j             
            
        A[i], A[min_idx] = A[min_idx], A[i] 
    return count
count=0
def mergeSort(A,low,high):
    if low<high:
        mid=int((low+high)/2)
        count+=mergeSort(A,low,mid)
        count+=mergeSort(A,mid+1,high)
        combine(A,low,mid,high)
    return count

def combine(arr, l, m, r): 
    count=0
    n1 = m - l + 1
    n2 = r- m   
    
    L = [0] * (n1) 
    R = [0] * (n2)   
   
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j]   
    
    i = 0     
    j = 0     
    k = l       
    count+=1
    while i < n1 and j < n2 : 
        
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1  
    return count
A=[5,4,3,2,1]
print(bubbleSort(A))
print(selectionSort(A))

print(mergeSort(A,0,len(A)))