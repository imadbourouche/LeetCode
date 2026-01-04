# Kth Smallest Element in a BST

Given the root of a Binary Search Tree (BST) and an integer `k`, return the `k`-th smallest value in the tree.

## Approach

1. Initialize a stack and push the root.
2. Traverse left until no more left children.
3. Pop from the stack:

   * Decrement `k`
   * If `k == 0`, return the node value
4. If the node has a right child, traverse its leftmost path.
5. Repeat until found.

## Complexity

* **Time:** `O(k)` average, `O(n)` worst case
* **Space:** `O(h)` where `h` is the tree height

## Notes

* No recursion → avoids stack overflow.
* Efficient for early termination when `k` is small.
* Assumes valid BST and `1 ≤ k ≤ number of nodes`.
