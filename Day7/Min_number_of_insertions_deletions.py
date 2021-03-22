class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def lcs(a,b,n,m):
            dp = [[0]*(m+1) for _ in range(n+1)]
            for i in range(1,n+1):
                for j in range(1,m+1):
                    if a[i-1]==b[j-1]:
                        dp[i][j] = 1+dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            #print(dp)
            return dp[n][m]
        
        n = len(word1)
        m = len(word2)
        
        len_lcs = lcs(word1,word2,n,m)
        #print(len_lcs)
        return abs(n-len_lcs)+abs(m-len_lcs)
        
