class Solution:
    def maxSubArray(self, nums) :
        res = -1
        sum1 = 0
        neg_arr = True
        for i in range(0,len(nums)):
            if nums[i]>0:
                neg_arr = False
            sum1 += nums[i]
            if sum1<0:
                sum1=0
            res=max(sum1,res)
        if neg_arr == True:
            return max(nums)
        return res
            
    
# https://leetcode.com/problems/maximum-subarray/
