# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stackp = []
        stackq = []
        if p:
           stackp.append([p, "root"])
        if q:
           stackq.append([q, "root"])
        while stackp and stackq:
            nodep, directionp = stackp.pop()
            nodeq, directionq = stackq.pop()
            if nodep.val != nodeq.val or directionp != directionq:
                return False
            nodep.left and stackp.append([nodep.left, "left"])
            nodep.right and stackp.append([nodep.right, "right"])
            nodeq.left and stackq.append([nodeq.left, "left"])
            nodeq.right and stackq.append([nodeq.right, "right"])
        if not stackp and not stackq:
            return True
        return False
