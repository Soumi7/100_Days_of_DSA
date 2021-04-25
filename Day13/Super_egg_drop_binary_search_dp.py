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
                l=1
                h=j
                ans = n
                while(l<=h):
                    mid =(l+h)//2
                    left = t[i-1][mid-1]
                    right = t[i][j-mid]
                    temp = 1 + max(left,right)
                    if left<right:
                        l=mid+1
                    else:
                        h=mid-1
                    ans = min(ans,temp)
                
                t[i][j] = ans
                    
        
    
        return t[k][n]
