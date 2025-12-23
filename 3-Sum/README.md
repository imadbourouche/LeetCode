# 3Sum 

Description: Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# My personal solution: Hash Map Approach

## My Approach

This solution treats the **3Sum** problem as a series of **Two Sum** sub-problems.

1. **Iterate through the array:** Pick an element `a` as the first part of our triplet.
2. **Define a target:** To satisfy , we need to find two other numbers  and  such that .
3. **Hash Map lookup:** For each remaining element, we use a hash map (`map_target`) to check if the complement needed to reach the target has already been seen.
4. **Duplicate Management:** * Used a `seen` set to skip the same "first" element.
    * Used a `local_seen` set to ensure unique pairs are found within the inner loop.



## Complexity Analysis

* **Time Complexity:** O(n^2)
    * We iterate through the list  times, and for each element, we perform a linear scan () to find the pairs.


* **Space Complexity:** O(n)
    * We use hash maps and sets to store visited numbers and potential targets, which scales linearly with the input size.



## Key Observations

This version is a **non-sorting approach**. While most optimal 3Sum solutions use a **Two-Pointer** method on a sorted array to reach  with  extra space, this hash map approach:

* Avoids the initial  sort.
* Requires more memory (space) to handle the duplicate sets and maps compared to the two-pointer method.