amount=27
coins=[1,2,5]

def coinChange(amount,denoms):
    #denoms.sort()
    dp=[[0]*(amount+1) for _ in range(len(coins))]
    dp[0]=[i//coins[0] for i in range(amount+1)]  

    for i in range(1,(len(coins))):     
        
        for j in range(1,amount+1):
            if coins[i]<=j:
                dp[i][j]=min(1+dp[i][j-coins[i]],dp[i-1][j])      
            else:  
                dp[i][j]=dp[i-1][j]
    
    return dp


def findCoins(dp):
    ans=[]
    i,j=len(dp)-1,len(dp[0])-1
    while i>=0 and j>=0:
        if dp[i][j]=dp[i-1][j]:
            i-=1
        else:
            




print(findCoins(coinChange(amount,coins)))


