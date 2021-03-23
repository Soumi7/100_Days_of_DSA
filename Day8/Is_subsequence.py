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
            lcs=""         
            while(i>0 and j>0):
                if a[i-1]==b[j-1]:
                    lcs=a[i-1]+lcs
                    i-=1
                    j-=1
                else:
                    if dp[i-1][j]<dp[i][j-1]:
                        j-=1
                    else:
                        i-=1
            return lcs
        if s=="":
            return True
        if t=="":
            return False
        lcs= lcs(s,t,len(s),len(t))
        print(lcs)
        if lcs==s:
            return True
        else:
            return False
                    
        
