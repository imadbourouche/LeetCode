# Invert Binary Tree (Iterative Stack Solution)

This solution inverts a binary tree by swapping the left and right children of every node.

## Approach

* Use an **iterative Depth-First Search (DFS)** with a stack.
* Start by pushing the root node onto the stack.
* While the stack is not empty:

  * Pop a node
  * Swap its left and right children
  * Push non-null children back onto the stack

## Why this works

* Every node is visited exactly once
* Swapping at each node guarantees the tree is fully inverted
* Avoids recursion depth limits

## Time & Space Complexity

* **Time:** `O(n)` — each node is processed once
* **Space:** `O(n)` — stack may hold up to all nodes in the worst case

## Other Possible Solutions

* **Recursive DFS**
* **Breadth-First Search (queue-based)**