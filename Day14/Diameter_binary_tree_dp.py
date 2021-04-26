# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = -1
        def solve(root):
            if root == None:
                return 0
            l = solve(root.left)
            r = solve(root.right)
            temp = 1 + max(l,r)
            self.ans = max(self.ans,l+r+1)
            return temp
        t = solve(root)
        return self.ans - 1
            
        
