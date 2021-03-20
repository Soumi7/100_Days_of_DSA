class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n= len(text1)
        m= len(text2)
        
                
        def lcs(a,b,n,m):
            if n==0 or m==0:
                return 0
            if a[n-1]==b[m-1]:
                return 1+lcs(a,b,n-1,m-1)
            else:
                return(max(lcs(a,b,n-1,m),lcs(a,b,n,m-1)))
            
        return lcs(text1,text2,n,m)
        
