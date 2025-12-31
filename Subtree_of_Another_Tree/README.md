# Subtree of Another Tree

This solution checks whether one binary tree (`subRoot`) is a **subtree** of another (`root`) using an **iterative traversal** approach.

It combines:

* **BFS** to scan candidate roots in `root`
* **DFS (stack-based)** to compare tree structures and values

## Approach

* Traverse the main tree (BFS)
    * Use a queue to visit each node in `root`
    * When a node’s value matches `subRoot.val`, treat it as a **candidate root**

* Compare trees iteratively (`isSameTree`)
    * see the solution here: [Same_Tree](../Same_Tree/solution.py)

## Complexity

* **Time:**

  * Worst case: `O(n * m)`

    * `n` = nodes in `root`
    * `m` = nodes in `subRoot`

* **Space:**

  * `O(h)` for stacks (tree height)