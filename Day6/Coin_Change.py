class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        t = [[9999999999999]*(amount+1) for _ in range(n+1)]
        w = amount
        
        for i in range(0,(w+1)):
            t[0][i] = 9999999999999
            
        for i in range(0,n+1):
            t[i][0] = 0
            
        for i in range(1,n+1):
            for j in range(0,w+1):
                if coins[i-1] <= j:
                    t[i][j] = min(1+t[i][j-coins[i-1]],t[i-1][j])
                else:
                    t[i][j] = t[i-1][j]
                    
        if t[n][w] == 9999999999999:
            return -1
        else:
            return t[n][w]
        
