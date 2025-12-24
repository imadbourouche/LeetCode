# Reorder List (Stack-based Solution)

Given the head of a singly linked list, reorder it **in-place** as:

```
L0 → L1 → … → Ln-1 → Ln
↓
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
```

You must **not modify node values**, only pointers.

### My solution

This solution uses a **stack** to access nodes from the end while iterating from the front.

#### Steps

1. Traverse the list and push all nodes onto a stack.
2. Use a pointer `tmp` starting from the head.
3. Repeatedly:

   * Pop the last node from the stack.
   * Insert it after `tmp`.
   * Move `tmp` two steps forward.
4. Stop when pointers meet or cross.
5. Explicitly terminate the list to avoid cycles.

### Key Conditions

* `v != tmp` → pointers haven’t met
* `v != tmp.next` → pointers haven’t crossed

These ensure correct termination for both even and odd length lists.


### Complexity

* **Time:** `O(n)`
* **Space:** `O(n)` (stack)
