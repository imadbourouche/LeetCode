# Longest Consecutive Sequence

This solution finds the length of the longest consecutive integer sequence in an array in **O(n)** time.

## Approach

* Store all numbers in a **set** for constant-time lookups and deletions.
* Iterate through each number and, if it hasn’t been processed:

  * Expand **left** (`i - 1`) and **right** (`i + 1`) to find the full consecutive sequence.
  * Remove visited numbers from the set to avoid reprocessing.
* Track the maximum sequence length found.

## Why it Works

* Each number is removed from the set **once**, ensuring linear time.
* Using a set avoids sorting and enables fast checks.

## Complexity

* **Time:** O(n)
* **Space:** O(n)
