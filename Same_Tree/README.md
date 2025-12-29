# Check if Two Binary Trees are the Same (Iterative DFS)

This solution determines whether two binary trees are **structurally identical** and have the **same node values** using an **iterative Depth-First Search (DFS)** approach with stacks.

## Approach

1. **Edge Case:** If both trees are empty (`None`), they are the same. If only one is empty, return `False`.
2. **Initialize Stacks:** Each tree has its own stack. Push the root nodes with a marker `"root"`.
3. **Iterative Traversal:**

   * Pop a node from each stack.
   * Compare their values and positions (`"left"`/`"right"`) to ensure structural match.
   * Push children into the respective stacks with their direction.
4. **Validation:**

   * If all nodes match and both stacks are empty, the trees are identical.
   * If any mismatch occurs or stack lengths differ, return `False`.

## Complexity

* **Time Complexity:** O(n) each node in both trees is visited once.
* **Space Complexity:** O(h) where `h` is the height of the tree (stack usage).


## Other Possible Solutions

1. **Recursive DFS:** Compare nodes recursively, also checking structure by comparing left and right children.
2. **Breadth-First Search (BFS):** Use queues to traverse both trees level by level and compare nodes.