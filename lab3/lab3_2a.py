def split(A,low,high):
    if low<high:
        mid=int((low+high)/2)
        split(A,low,mid)
        split(A,mid+1,high)
        combine(A,low,mid,high)



def combine(arr, l, m, r): 
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
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1  
   
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1  
   
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1

A=[]
n=int(input("Enter n"))
for i in range(n):
    A.append(int(input("Enter element")))

split(A,0,len(A)-1)
print(A)