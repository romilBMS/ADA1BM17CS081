def binarySqrt(n) -> int:
    l,h=0,n
    sqrt=0
    while l<=h:
        mid=int((l+h)/2)    
        if(mid*mid)==n:
            sqrt=mid
            return sqrt
        elif mid*mid<n:
            sqrt=mid
            l=mid+1
        else:
            h=mid-1

    return sqrt



n=int(input("Enter the number"))
print("Square root is",binarySqrt(n))
