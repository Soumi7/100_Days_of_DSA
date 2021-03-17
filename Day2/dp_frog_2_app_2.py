import sys
sys.setrecursionlimit(10**6)
n,k = list(map(int,input().split()))
arr = list(map(int,input().split()))
         
dp = [sys.maxsize]*n
dp[0] = 0
for i in range(n):
    for j in range(i+1,i+k+1):
        if j<n:
            dp[j] = min(dp[j],dp[i]+abs(arr[i]-arr[j]))


print(dp[n-1])
