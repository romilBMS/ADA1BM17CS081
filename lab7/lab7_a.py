def findLCS(str1, str2):
    cList1,cList2=list(str1), list(str2)
    L=[]
    for i in range(len(cList1)+1):
        L.append([0]*(len(cList2)+1))    

    for i in range(1,len(cList1)+1):  #str1
        for j in range(1,len(cList2)+1):  #str2
            if cList1[i-1] == cList2[j-1]:
                L[i][j]=L[i-1][j-1]+1
            else:
                L[i][j]= max(L[i-1][j], L[i][j-1])
    
    print("Length of LCS:", L[i][j])   
    # print(L)
    

    res=[]    
    while i>0 and j>0:
        if cList1[i-1]== cList2[j-1]:          
            res.append(cList1[i-1])
            i-=1
            j-=1
        else:
            if L[i][j]==L[i-1][j]:
                i-=1
            else:
                j-=1
    res.reverse()
    print(res)       
     
str1,str2= input("Enter string:"),input("Enter string:")
findLCS(str1,str2)

    



