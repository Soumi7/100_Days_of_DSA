class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        t = [[-1]* (n+1)  for _ in range(k+1)]
        #print(t)
    
        def solve(egg,floor):
            #print(egg,floor)
            if t[egg][floor]!=-1:
                return t[egg][floor]
            if egg == 1:
                return floor
            if floor == 0:
                return 0
            if floor == 1:
                return 1
            min1 = sys.maxsize
            for k in range(1,floor+1):
                if t[egg-1][k-1]!=-1:
                    low =  t[egg-1][k-1]
                else :
                    low = solve(egg-1,k-1)
                    t[egg-1][k-1] = low
                if t[egg][floor-k]!=-1:
                    high =  t[egg][floor-k]
                else :
                    high = solve(egg,floor-k)
                    t[egg][floor-k] =  high
                
                temp = 1 + max(low,high)
                min1=min(min1,temp)
                
            t[egg][floor]=min1    
            return min1
        return solve(k,n)
