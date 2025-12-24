# Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.

## Two pass Algorithm
1. First, traverse the entire linked list to count the total number of nodes.
2. Calculate the position of the node to be removed from the start of the list using the formula: `position_from_start = total_nodes - n + 1`.
3. Traverse the linked list again to reach the node just before the one to be removed.
4. Adjust the `next` pointer of the previous node to skip the node to be removed.
5. Return the head of the modified linked list.

### Complexity
- Time Complexity: O(L), where L is the length of the linked list. We traverse the list twice.
- Space Complexity: O(1), as we are using only a constant amount of extra space.

## One pass Algorithm
1. Use two pointers, `left` and `right`, both initially pointing to the head of the linked list.
2. Move the `right` pointer `n` nodes ahead in the list.
3. If `right` becomes `None`, it means we need to remove the head node. Return `head.next`.
4. Else: Move both pointers one node at a time until the `right` pointer will be None, each time hold a previous node which is the node just before the `left` pointer.
5. At this point, the `left` pointer will be pointing to the node to be removed (why because the distance between the right and left pointers is n).
6. Remove the node pointed to by `left` by adjusting the `next` of the previous pointer to the node after `left`.

### Complexity
- Time Complexity: O(L), where L is the length of the linked list. We traverse the list once.
- Space Complexity: O(1), as we are using only a constant amount of extra space.