class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n= len(text1)
        m= len(text2)
        
        dp = [ [-1] * ( m +1 ) for i in range(0,n+1) ]
        
        #print(dp)
        
                
        def lcs(a,b,n,m):
            if n==0 or m==0:
                return 0
            #print(n,m)
            if dp[n][m]!=-1:
                return dp[n][m]
            if a[n-1]==b[m-1]:
                dp[n][m] = 1+lcs(a,b,n-1,m-1)
                return dp[n][m]
            else:
                dp[n][m] = max(lcs(a,b,n-1,m),lcs(a,b,n,m-1))
                return dp[n][m]
            
        #print(dp[n][m])
            
        return lcs(text1,text2,n,m)
        
