class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        k=sum(nums)
        if k%2!=0:
            return False
        else:
            
            
            def subsetsum(arr,n,w):
                if dp[n][w]!=-1:
                    return dp[n][w]
                if n==0 and w==0:
                    return True
                if w>0 and n==0:
                    return False
                if arr[n-1]<=w:
                    dp[n][w] = (subsetsum(arr,n-1,w-arr[n-1]) or subsetsum(arr,n-1,w))
                    return dp[n][w]
                else:
                    dp[n][w] = subsetsum(arr,n-1,w)
                    return dp[n][w]
            
            dp = [  [-1]  *  (  (k//2)   +1  )  ]*(len(nums)+1)
            #print(dp)
            
                
            return subsetsum(nums,len(nums),k//2)
        
        
        
