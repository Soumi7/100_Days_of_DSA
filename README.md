# 100_Days_of_DSA

Day 1 :
- https://leetcode.com/problems/copy-list-with-random-pointer/
- https://atcoder.jp/contests/dp/tasks/dp_a  - To solve the problem of errors, use sys.setrecursionlimit(10**6).

Day 2 :
- https://leetcode.com/problems/3sum/
- https://atcoder.jp/contests/dp/tasks/dp_b So in atcoder if I need to tackle the tle, have to select language as PyPy3. :)

Day 3 :
- https://leetcode.com/problems/trapping-rain-water/

Day 4 :
- https://leetcode.com/problems/partition-equal-subset-sum/
  - Declare array like this ```dp = [  [False]  *  (  (k//2)   +1  ) for i in range(0,len(nums)+1) ]```
  - Declaring like ```dp = [  [False]  *  (  (k//2)   +1  )  ]*(len(nums)+1)``` creates instances of the same intial list, so change in any of the indexes updated all the instances in other rows.

Day 5 :
- https://leetcode.com/problems/target-sum/ : Remember the check for ```(array_sum+diff) %2 ==1: return 0``` as in that case no subset exists with that sum.

Day 6 :
- https://leetcode.com/problems/coin-change/
- https://leetcode.com/problems/longest-common-subsequence/ (subsequence)
- https://leetcode.com/problems/maximum-length-of-repeated-subarray/submissions/ (substring)
       
Day 7 :
- https://leetcode.com/problems/shortest-common-supersequence/
- https://leetcode.com/problems/delete-operation-for-two-strings/

Day 8 :
- https://leetcode.com/problems/longest-palindromic-subsequence/
- https://leetcode.com/problems/is-subsequence/ - Dont need to find lcs, just length will do.
- https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

Day9 :
- https://leetcode.com/problems/palindrome-partitioning-ii/

Day 10 :
- https://leetcode.com/problems/longest-palindromic-substring/

Day 11 :
- https://www.interviewbit.com/problems/evaluate-expression-to-true/
