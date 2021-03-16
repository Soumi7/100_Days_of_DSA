class Solution:
    def trap(self, height: List[int]) -> int:
        from_left_max=[]
        min_arr=[]
        from_right_max= []
        max_l=-10000000000000000000000
        max_r=-10000000000000000000000
        n = len(height)
        for i in range(0,n):
            max_l=max(max_l,height[i])
            from_left_max.append(max_l)
            max_r = max(max_r,height[n-i-1])
            from_right_max.insert(0,max_r)
            
        for j in range(0,n):
            min_arr.append(  min  (  from_left_max[j],from_right_max[j]  )   )
            
        res=0
            
        for i in range(0,n):
            res+=min_arr[i]-height[i]
            
        return res
            
            
            
        
            
            
        
