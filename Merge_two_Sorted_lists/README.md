# Merge Two Sorted Linked Lists

### Description

This algorithm merges two **sorted singly linked lists** into one sorted linked list.
It reuses existing nodes and does not create new ones.

### Approach

1. Handle edge cases where one of the lists is `None`.
2. Select the smaller head node to initialize the result list.
3. Traverse both lists, always attaching the smaller current node.
4. When one list ends, append the remaining nodes of the other list.

### Complexity

* **Time Complexity:** `O(n + m)`
* **Space Complexity:** `O(1)` (in-place, no extra nodes)
