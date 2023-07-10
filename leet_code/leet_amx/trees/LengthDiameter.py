# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0
        def traverseTree(root):
            nonlocal res
            if not  root:
                return 0
            left = traverseTree(root.left)
            right = traverseTree(root.right)
            res = max(res,left+right)
            return 1 + max(left,right)
        traverseTree(root)
        return res