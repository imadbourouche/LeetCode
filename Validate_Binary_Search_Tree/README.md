# Validate Binary Search Tree (BST)

This solution validates a Binary Search Tree using **Breadth-First Search (BFS)** with explicit value bounds for each node.

Instead of only comparing a node with its direct parent, we track the **allowed value range** (`min`, `max`) that each node must satisfy based on BST rules.

## Approach

1. Initialize a queue with:

   * `(root, -∞, +∞)` 
2. While the queue is not empty:

   * Pop `(node, min, max)`
   * If `node.val` is outside `(min, max)` → return `False`
   * Push:
     * Left child with updated upper bound (update max with node.val)
     * Right child with updated lower bound (update min with node.val)
3. If all nodes are valid → return `True`

## Time & Space Complexity

* **Time:** `O(n)` — each node visited once
* **Space:** `O(n)` — queue in worst case
