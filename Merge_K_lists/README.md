# Merge K Sorted Linked Lists

This solution merges **K sorted linked lists** into a single sorted linked list by repeatedly merging two lists at a time.

### Approach

* `mergeTwoLists` merges two sorted linked lists using an **iterative two-pointer technique**.
* `mergeKLists` merges all lists by:

  * Starting with the first list
  * Iteratively merging it with the next list

### Complexity

* **Time:** `O(k * n)`

  * `k` = number of lists
  * `n` = total number of nodes across all lists
* **Space:** `O(1)` extra space (in-place merge)

