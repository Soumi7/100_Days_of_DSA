class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        k=sum(nums)
        if k%2!=0:
            return False
        else:
            def subsetsum(arr,n,w):
                if n==0 and w==0:
                    return True
                if w>0 and n==0:
                    return False
                if arr[n-1]<=w:
                    return (subsetsum(arr,n-1,w-arr[n-1]) or subsetsum(arr,n-1,w))
                else:
                    return subsetsum(arr,n-1,w)
                
            return subsetsum(nums,len(nums),k/2)
        
        
        
