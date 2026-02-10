# Meeting Rooms II – LeetCode Solution (Go)

Given an array of meeting time intervals `[[s1,e1],[s2,e2],...]`, determine the **minimum number of conference rooms required**.

## Solution Approach

1. **Sort intervals by start time.**
2. Maintain a slice of `buckets`, each representing the **end time of a meeting currently occupying a room**.
3. Iterate through the intervals:

   * If a meeting can reuse an existing room (its start time ≥ room’s end time), update that room’s end time.
   * Otherwise, allocate a new room (append a new end time to `buckets`).
4. Return the number of `buckets` as the **minimum rooms required**.

### Key Points

* **Time complexity:** `O(n^2)` in worst case due to nested loops over `buckets`.
* **Space complexity:** `O(n)` for the `buckets` slice.
* Works efficiently for small to medium inputs. For large inputs, a **priority queue (min-heap)** can improve performance to `O(n log n)`.
