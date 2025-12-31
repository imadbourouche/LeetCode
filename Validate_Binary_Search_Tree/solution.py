# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = deque([(root, float("-inf"), float("inf"))])
        while queue:
            node, left_boundry, right_boundry = queue.popleft()
            if left_boundry < node.val < right_boundry:
                node.left and queue.append([node.left, left_boundry, node.val])
                node.right and queue.append([node.right, node.val, right_boundry])
            else:
                return False
        return True