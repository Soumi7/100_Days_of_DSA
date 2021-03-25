class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        n = len(nums)
        for i in range(0,n-2):
            if i==0 or (i>0 and nums[i]!=nums[i-1]):
                low = i+1
                high = n-1
                sum1 = 0-nums[i]
                while(low<high):
                    #print(low,high)
                    if (nums[low] + nums[high])==sum1:
                        res.append([nums[i],nums[low],nums[high]])
                        
                        while(low < high and nums[low] == nums[low+1]) :
                            low+=1
                        while(low < high and nums[high] == nums[high-1]) :
                            high-=1
                        low+=1
                        high-=1
                        
                    elif (nums[low] + nums[high] )< sum1 :
                        low+=1
                    else:
                        high-=1
                            
        #print(res)
        return res
                    
                
            
        
