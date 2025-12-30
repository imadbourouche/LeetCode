# Level-Order Traversal of a Binary Tree

Given a binary tree, return its **level-order traversal** (i.e., traverse the tree level by level from left to right).

## Solution

We use a **queue** (FIFO) to implement **Breadth-First Search (BFS)**:

1. Initialize a queue with the root node.
2. While the queue is not empty:

   * Process all nodes at the current level.
   * Append their values to a `level` list.
   * Add their children to the queue for the next level.
3. Append each `level` list to the result `res`.
4. Return `res`.

## Complexity

* **Time:** O(n) — each node is processed exactly once.
* **Space:** O(n) — the queue can hold up to all nodes in the worst case (In a perfect or complete binary tree, the last level has roughly n/2 nodes).