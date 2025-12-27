# Find Minimum in Rotated Sorted Array

## Problem

Given a rotated sorted array of **unique integers**, return the minimum element in **O(log n)** time.

## Approach

* Use **binary search**.
* If the current subarray is already sorted (`nums[l] <= nums[r]`), the left element is the minimum.
* Otherwise:

  * If `nums[mid] >= nums[l]`, the minimum is in the **right half**.
  * Else, it’s in the **left half**.
* Narrow the search until one element remains.

## Time & Space

* **Time:** `O(log n)`
* **Space:** `O(1)`


## Optimized Version

This version applies a pure lower-bound binary search without pre-checks. It directly converges to the minimum by comparing nums[mid] with nums[r].

- Time: O(log n)
- Space: O(1)