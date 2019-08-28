def QS(A ,low , high):
    if low<high:
        pivot_pos=part(A, low , high)
        QS(A,low,pivot_pos-1)
        QS(A, pivot_pos+1,high)

def part(A, low, high):
    pivot=A[low]
    i=low+1
    j=high
    while(True):
        while A[i]<=pivot and i<=high:
            i+=1
        while A[j]>pivot and j>=low:
            j-=1
        if i<j:
            A[i],A[j]=A[j],A[i]
        else:
            A[low]=A[j]
            A[j]=pivot
            return j
A=[]
n=int(input("Enter n"))
for i in range(n):
    A.append(int(input("Enter element")))

QS(A,0,len(A)-1)
print(A)



    
    