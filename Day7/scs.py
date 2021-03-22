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
            lcs=""            
            while(i>0 and j>0):
                if a[i-1]==b[j-1]:
                    lcs=a[i-1]+lcs
                    i = i-1
                    j = j-1
                else:
                    if dp[i-1][j]>dp[i][j-1]:
                        i=i-1
                    else:
                        j=j-1
                    
            return lcs
        
        n=len(str1)
        m=len(str2)
        lcs = lcs(str1,str2,n,m)
        print(lcs)
        k=len(lcs)
        scs=""
        p1=0
        p2=0
        p3=0
        while(p1<n and p2<m and p3<k):
            while(str1[p1]!=lcs[p3]):
                scs = scs + str1[p1]
                p1+=1
            while(str2[p2]!=lcs[p3]):
                scs = scs + str2[p2]
                p2+=1
            scs+=lcs[p3]
            p3+=1
            p1+=1
            p2+=1
        print(scs)
        while(p1<n):
            scs+=str1[p1]
            p1+=1
        while(p2<m):
            scs+=str2[p2]
            p2+=1
        print(scs)
                
        return (scs)
                        
                    
                
        
