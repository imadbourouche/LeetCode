## Merge Intervals (Go)

Given a list of intervals, merge all overlapping intervals and return the resulting non-overlapping intervals sorted by start time.

### Approach

1. **Sort** intervals by their start value.
2. Initialize the result with the first interval.
3. Iterate through the remaining intervals:

   * If the current interval overlaps with the last interval in `res`, merge them by extending the end.
   * Otherwise, append the interval to `res`.
4. Return the merged result.

### Algorithm

* Sorting ensures intervals are processed in order.
* Only the **last merged interval** needs to be checked for overlap.
* Time-optimal greedy approach.

### Time & Space Complexity

* **Time:** `O(n log n)` (due to sorting)
* **Space:** `O(n)` (for the result slice)

