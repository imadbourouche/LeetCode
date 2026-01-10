# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root: 
            return ""
        queue = deque([(root, "r")])
        res = ""
        while queue:
            node, direction = queue.popleft()
            if not node:
                res += direction + "-"
            else:
                res += direction + str(node.val)
                queue.append([node.left, "L"])
                queue.append([node.right, "R"])
            if direction == "R":
                res += "#"
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(data)
        if not data:
            return None
        i = data.find("L")       
        root = TreeNode()
        root.val = data[1 : i]
        queue = deque([root])
        while queue and i < len(data):
            node = queue.popleft()
            node.left , node.right = None, None
            end = data.find("#", i)
            j = data.find("R", i, end)
            left_val = data[i+1: j]
            right_val = data[j+1: end]
            if left_val != "-":
                node.left= TreeNode()
                node.left.val = left_val
                queue.append(node.left)
            if right_val != "-":
                node.right= TreeNode()
                node.right.val = right_val
                queue.append(node.right)
            i = end + 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))