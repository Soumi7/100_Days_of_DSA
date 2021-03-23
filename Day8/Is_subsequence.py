class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def lcs(a,b,n,m):
            dp = [[0]*(m+1) for _ in range (n+1)]
            for i in range(1,n+1):
                for j in range(1,m+1):
                    if a[i-1]==b[j-1]:
                        dp[i][j] = 1+dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            return dp[n][m]
        if s=="":
            return True
        if t=="":
            return False
        n = len(s)
        m = len(t)
        lcs= lcs(s,t,n,m)
        
        if lcs==n:
            return True
        else:
            return False
                    
        
