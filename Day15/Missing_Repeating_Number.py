# https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/



class Solution:
    def findTwoElement( self,arr, n): 
        sum_n = n * (n+1) * (0.5)
        sum_squares_n = n * (n+1) * ((2*n)+1) * (1/6)
        sum_arr = sum(arr)
        sum_squares_arr = 0
        for i in range(0,n):
            sum_squares_arr += arr[i]**2
        # print(sum_n)
        # print(sum_squares_n)
        # print(sum_arr)
        # print(sum_squares_arr)
        A = (sum_n - sum_arr)   + (  (sum_squares_n - sum_squares_arr)  /  (sum_n - sum_arr)  )   
        A = A * 0.5
        B = A  - sum_n + sum_arr
        return [int(B),int(A)]
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends
