# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")
        def dfs(root):
            nonlocal max_sum
            if not root:
                return 0
            left_tree_sum = max(dfs(root.left), 0)
            right_tree_sum = max(dfs(root.right), 0)
            max_sum = max(max_sum, root.val + left_tree_sum + right_tree_sum)
            return max(root.val + left_tree_sum, root.val + right_tree_sum)
        dfs(root)
        return max_sum