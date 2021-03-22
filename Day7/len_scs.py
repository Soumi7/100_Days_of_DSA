class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        def lcs(a,b,n,m):
            dp = [[0]*(m+1) for _ in range (n+1)]
            for i in range(1,n+1):
                for j in range(1,m+1):
                    if a[i-1]==b[j-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            return dp[n][m]
        
        n=len(str1)
        m=len(str2)
        lcs_len = lcs(str1,str2,n,m)
        return (n+m-lcs_len)
                        
                    
                
        
