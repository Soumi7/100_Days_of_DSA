import sys
sys.setrecursionlimit(10**6)
N,K = list(map(int,input().split()))
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
    min_right = sys.maxsize
    for k in range(2,K+1):      
      if i+k<N:
        right1 = abs(arr[i]-arr[i+k])+recur(i+k)      
        min_right = min(min_right,right1)
    dp[i] = min(left,min_right)
    return min(left,min_right)
      
  print(recur(0))
