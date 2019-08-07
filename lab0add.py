def binarySearch(num_array,h,key) -> int:
    mid=0
    l=0
    while l<=h:
        mid=int((l+h)/2)
        if(key== num_array[mid]):
            return 1
        elif(key>num_array[mid]):
            l=mid+1
        else:
            h=mid-1

    return -1

def readFile():
    count=0
    f=open("testCase.txt")
    f1=f.readlines()
    for i in f1:
        if count==0:
            noOfTextCases=int(f1.read())
            count=count+1
        
        for i in range(0,2*numberOfTextCases):
            

        
        
        

readFile()
