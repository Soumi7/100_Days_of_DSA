class Solution:
    def minCut(self, s: str) -> int:
        def isPalindrome(s,i,j):
            if i==j:
                return True
            while(i<=j):
                #rint(i,j)
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        def solve(s,i,j):
            if dp[i][j]!=-1:
                return dp[i][j]
            if i>=j:
                return 0
            if pal[i][j]!=-1:
                if pal[i][j]:
                    dp[i][j]=0
                    return 0
            else :
                pal[i][j]=isPalindrome(s,i,j)
                if pal[i][j]:
                    dp[i][j]=0
                    return 0
            mi = 99999999999999999999999
            for k in range(i,j):
                if dp[i][k]!=-1:
                    c1 = dp[i][k]
                else:
                    c1 = solve(s,i,k)
                    dp[i][k]= solve(s,i,k)
                if dp[k+1][j]!=-1:
                    c2= dp[k+1][j]
                else:
                    c2= solve(s,k+1,j)
                    dp[k+1][j]= solve(s,k+1,j)
                temp = c1 + c2 + 1
                mi = min(mi, temp)
            return mi
        n=len(s)
        dp = [[-1]*(n+1) for _ in range(n+1)]
        pal = [[-1]*(n+1) for _ in range(n+1)] 
        return (solve(s,0,len(s)-1))
