import sys
sys.setrecursionlimit(10**6)
N = int(input())
arr = list(map(int,input().split()))
         
if N==2 :
  print(abs(arr[0]-arr[1]))
elif N==1:
  print(arr[0])
elif N==0:
  print(0)
else:
  dp = [-1] * N
   
  def recur(i):

    if i==(N-1):
      return 0
    if i>=N:
      return sys.maxsize
    if dp[i]!=-1:
      return dp[i]
    left = abs(arr[i]-arr[i+1])+recur(i+1)
    right = sys.maxsize
    if (i+2)<N:
      right = abs(arr[i]-arr[i+2])+recur(i+2)      
    dp[i] = min(left,right)
    return min(left,right)
      
  print(recur(0))
      
        
      
      
                                     
