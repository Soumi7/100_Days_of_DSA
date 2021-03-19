class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        s = sum(nums)
        print(s)
        if (s+S)%2==1:
            return 0
        w = (s+S)//2
        
        n = len(nums)
        print(n,w)
        dp =[]
        if S>s :
            return 0
        
        for i in range(0,n+1):
            k=[]
            for j in range(0,w+1):
                k.append(0)
            dp.append(k)
            
        #print(dp)
        
        for i in range(0,w+1):
            dp[0][i] = 0
        for i in range(0,n+1):
            dp[i][0] = 1
        for i in range(1,n+1):
            for j in range(0,w+1):
                if nums[i-1]<= j :
                    dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        #print(dp)
        return dp[n][w]
            
            
        
        
