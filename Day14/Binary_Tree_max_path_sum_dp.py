# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = -sys.maxsize-1
        def solve(root):
            if root == None:
                return 0
            l = solve(root.left)
            r = solve(root.right)
            temp = max(root.val,root.val + max(l,r))
            res = max(temp,l+r+root.val)
            self.ans = max(self.ans,res)
            return temp
        t = solve(root)
        return self.ans
            
        
