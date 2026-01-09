## Maximum Path Sum in Binary Tree

Given a binary tree, find the **maximum path sum**.
A path can start and end at any node, but it must go downwards (parent → child connections).

## Approach

1. **Initialize global maximum**
   * `max_sum = -∞`
   * Stores the best path sum found anywhere in the tree.

2. **Start DFS from the root**

   * DFS returns the **maximum path sum that can be extended to the parent**.

    * **Base case**

        * If the node is `None`, return `0`.

    * ***Process left subtree**
        * Recursively compute left gain.
        * If the gain is negative make it 0.

    * **Process right subtree**
        * Same logic as left

    * ***Update global maximum**
        * Consider a path **passing through the current node**: `node.val + left_gain + right_gain`
        * Update `max_sum` if this is larger.

    * **Return value to parent**
        * Only **one side** can be extended upward (path cannot fork): `max(node.val + left_gain, node.val + right_gain)`

3. **After DFS completes**
   * `max_sum` contains the maximum path sum in the tree.

## Complexity

* **Time:** `O(n)` — each node visited once
* **Space:** `O(h)` — recursion stack (`h` = tree height)