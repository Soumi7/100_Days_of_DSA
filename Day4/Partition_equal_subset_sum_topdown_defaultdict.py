import numpy as np
import collections
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        k=sum(nums)
        if k%2!=0:
            return False
        else:         
            def subsetsum(arr,n,w):
                for i in range(0,w+1):
                    dp[0][i] = False                    
                for j in range(0,n+1):
                    dp[j][0] = True
                for i in range(1,n+1):
                    for j in range(0,w+1):
                        if arr[i-1] <= j:
                            dp[i][j] = (dp[i-1][j-arr[i-1]]) or (dp[i-1][j])
                        else:
                            dp[i][j] = dp[i-1][j]                                                                
                return dp[n][w]
            dp = collections.defaultdict(dict)                
            return subsetsum(nums,len(nums),k//2)
        
        
        
