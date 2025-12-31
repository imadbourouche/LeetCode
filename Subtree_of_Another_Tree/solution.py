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

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.val == subRoot.val:
                if self.isSameTree(node, subRoot):
                    return True
            node.left and queue.append(node.left)
            node.right and queue.append(node.right)
        return False
        
    
    # Serialization method
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(root: Optional[TreeNode]) -> str:
            if root == None:
                return "$#"

            return ("$" + str(root.val) + serialize(root.left) + serialize(root.right))
        if not subRoot:
            return True
        if not root and subRoot:
            return False
        l = serialize(root)
        s = serialize(subRoot)

        if s in l:
            return True
        return False
        