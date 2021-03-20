class Solution:
    def findLength(self, A, B) -> int:
        n= len(A)
        m= len(B)
        
        dp = [ [0] * ( m +1 ) for i in range(n+1) ]
        
        for i in range(0,n+1):
            dp[i][0]=0
        for i in range(0,m+1):
            dp[0][i]=0
        max1=-1
        for i in range(1,n+1):
            for j in range(1,m+1):
                if A[i-1]==B[j-1]:
                    dp[i][j]  = 1 + dp[i-1][j-1]
                    max1=max(max1,dp[i][j])
                
        if max1==-1:
            return 0
        else:
            return max1
        
        
