class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        t = [[-1]* (n+1)  for _ in range(k+1)]
       
        
        for i in range(0,k+1):
            t[i][0]=0
            t[i][1]=1
            
        for i in range(0,n+1):
            t[0][i] = 0
            t[1][i] = i
            
        
        for i in range(2,k+1):
            for j in range(2,n+1):
                ans = sys.maxsize
                for x in range(1,n+1):
                    ans = min(ans,1 + max(t[i-1][x-1],t[i][j-x]))
                t[i][j] = ans
                    
        
    
        return t[k][n]
