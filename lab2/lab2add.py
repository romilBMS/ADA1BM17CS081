def findPivot(arr, low, high):
    if (high < low):
         return -1

    if (high == low):
         return low

    mid = int((low + high)/2)

    if (mid < high and arr[mid] > arr[mid + 1]):
        return mid

    if (mid > low and arr[mid] < arr[mid - 1]):
        return (mid-1)

    if (arr[low] >= arr[mid]):
        return findPivot(arr, low, mid-1);

    return findPivot(arr, mid + 1, high);



def binarySearch(num_array,key) -> int:
    mid=0
    l=0
    h=len(num_array)-1
    while l<=h:
        mid=int((l+h)/2)
        if(key== num_array[mid]):
            return 1
        elif(key>num_array[mid]):
            l=mid+1
        else:
            h=mid-1

    return -1

def findKey(A,key):
    pivot=findPivot(A,0,len(A))
    if(pivot!=len(A)-1):
        if key<A[0]:
            print(binarySearch(A[(pivot+1):],key))
        else:
            print(binarySearch(A[:pivot+1],key))
    else:
        print(binarySearch(A,key))

A=[1,2,3,4,5,-1,0]
findKey(A,4)
