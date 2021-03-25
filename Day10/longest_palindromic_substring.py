class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def expand(s,i,j):
            while i>=0 and j<len(s) and s[i]==s[j] :
                i-=1
                j+=1
            return j-i-1
        start = 0
        end = 0
        for i in range(0,n):
            l1 = expand(s,i,i)
            l2 = expand(s,i,i+1)
            m = max(l1,l2)
            if m > (end - start):
                start = i - ((m-1)//2) 
                end = i + (m//2 )
                
        return s[start:end+1]
                
