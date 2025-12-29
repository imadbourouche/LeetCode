# Max Depth of Binary Tree (Iterative BFS Solution)

This solution calculates the **maximum depth of a binary tree** using an **iterative Breadth-First Search (BFS)** approach with a queue.

## Approach

1. **Edge Case:** If the tree is empty (`root is None`), return `0`.
2. **Initialize Queue:** Start with the root node in a queue.
3. **Level-by-Level Traversal:**

   * Increment a `depth` counter for each level.
   * For each node at the current level, remove it from the queue and add its children to the queue.
4. **Return Depth:** After traversing all levels, `depth` contains the maximum depth of the tree.

## Complexity

* **Time Complexity:** O(n) each node is visited once.
* **Space Complexity:** O(w) where `w` is the maximum width of the tree (number of nodes at the widest level).

## Other Solutions

1. **Recursive Depth-First Search (DFS):** Use recursion to find the depth of left and right subtrees, returning `1 + max(left_depth, right_depth)`.
2. **Iterative DFS (Stack-based):** Traverse the tree with a stack, keeping track of the depth for each node.
