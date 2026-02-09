# Non-Overlapping Intervals

Given a list of intervals, return the **minimum number of intervals to remove** so that the remaining intervals are **non-overlapping**.

Two intervals overlap if one starts before the other ends.

## Approach (Greedy)

Greedy strategy: always keep the interval with the earliest end when overlap occurs.

### Steps

1. Sort intervals by **start time**.
2. Traverse intervals using two pointers:

   * `i`: index of the last kept interval
   * `j`: current interval
3. If `intervals[i]` overlaps with `intervals[j]`:

   * Increment removal count
   * Keep the interval with the **smaller end**
4. Otherwise, move forward normally.

This ensures maximum room for future intervals.

## Why It Works

* Overlapping intervals compete for time.
* Keeping the one that ends earlier reduces future conflicts.
* Local optimal choice → global optimal solution.

## Complexity

* **Time:** `O(n log n)` (sorting)
* **Space:** `O(1)` extra space (in-place)
