import heapq
def smallestRange(nums):
        k = len(nums)
        ans = []
        heap = [(row[0],i,0) for i,row in enumerate(nums)]
        
        heapq.heapify(heap)
        
        right = max(row[0] for row in nums)
        while heap:
            # the smallest on the top
            left,i,j = heapq.heappop(heap)
            if not ans or right-left < ans[1]-ans[0]:
                ans = [left,right]
            if j + 1 == len(nums[i]):
                return ans
            right = max(right,nums[i][j+1])
            heapq.heappush(heap,(nums[i][j+1],i,j+1))
        return ans

# k=int(input("Enter k:"))
# print("Enter",k,"lists")
# nums=[]
# for i in range(k):
#     nums.append(list(map(int,input().split(','))))
nums=[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
print(smallestRange(nums))
# list[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]


        