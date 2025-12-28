Here’s a concise README for your solution:

---

# Rotated Sorted Array Search

This repository contains a Python solution for efficiently searching a target value in a **rotated sorted array**. The solution uses a combination of **finding the pivot** and **binary search**.

## Problem

Given a sorted array that has been rotated at some unknown pivot, implement a function to find the index of a given target. Return `-1` if the target is not present.

## Solution

The solution involves two main steps:

1. **Find the pivot**: Identify the index of the smallest element in the rotated array. This divides the array into two sorted subarrays. Algorithm in [Find_Minimum_in_Rotated_Sorted_Array](../Find_Minimum_in_Rotated_Sorted_Array/solution.py)
2. **Binary search**: Perform a standard binary search on the appropriate subarray where the target could be present.


## Complexity

* **Time Complexity**: `O(log n)`
* **Space Complexity**: `O(1)`