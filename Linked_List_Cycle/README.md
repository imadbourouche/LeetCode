# Linked List Cycle Detection

### My Solution

* I implemented a solution that detects a cycle by **marking visited nodes**.
* Each node’s `val` is set to `None` when visited.
* If a node with `val == None` is encountered again, a cycle exists.

### Complexity 
* Time Complexity: O(n) - Each node is visited at most once.
* Space Complexity: O(1) - No extra space used.

### Cons of This Approach

* ❌ Modifies the input linked list
* ❌ Fails if `val` can naturally be `None`
* ❌ Corrupts data (unsafe in production)

## Better Solution (Recommended)

### Floyd’s Cycle Detection (Slow & Fast Pointers)

### Why This Is Better

* ✅ O(n) time
* ✅ O(1) space
* ✅ Does not modify the list