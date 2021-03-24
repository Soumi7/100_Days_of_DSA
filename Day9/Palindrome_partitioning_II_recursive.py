class Solution:
    def minCut(self, s: str) -> int:
        def isPalindrome(s,i,j):
            while(i<=j):
                #rint(i,j)
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        def solve(s,i,j):
            if i>=j:
                return 0
            if isPalindrome(s,i,j):
                return 0
            mi = 99999999999999999999999
            for k in range(i,j):
                temp = solve(s,i,k) + solve(s,k+1,j) + 1
                mi = min(mi, temp)
            return mi
        
        return (solve(s,0,len(s)-1))
