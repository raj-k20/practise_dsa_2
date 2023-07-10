# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

    #iterative
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        tstack = [[root,1]]
        res = 0
        while tstack:
            node,depth = tstack.pop()
            if node:
                res=max(res,depth)
                tstack.append([node.left,depth+1])
                tstack.append([node.right,depth+1])