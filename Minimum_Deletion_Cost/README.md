# Minimum Deletion Cost for Equal Characters

## Problem Overview

Given a string `s` and an integer array `cost`, the goal is to delete characters until the string contains only **equal characters** (e.g., "aaaa" or "bbb"). We want to achieve this with the **minimum total deletion cost**.

## Solution Logic: The "Max-Weight" Strategy

To minimize the deletion cost, we need to **maximize the cost of the characters we keep**.

1. **Calculate Total Cost:** First, find the sum of all deletion costs in the array.
2. **Group by Character:** As we iterate through the string, we sum the costs for each unique character (e.g., total cost for all 'a's, all 'b's, etc.).
3. **The Subtraction Rule:** The cost to delete everything *except* a specific character group is:
    - Deletion Cost = Total Cost - Total Cost of that Character Group

4. **Find the Minimum:** By keeping the character group with the **highest cumulative cost**, we automatically arrive at the minimum deletion cost.

## Complexity Analysis

* **Time Complexity:** O(n)
    * We perform one pass to sum the costs and one pass to iterate through the string.


* **Space Complexity:** O(1)
    * The hash map stores at most 26 keys (for English lowercase letters), which is constant space regardless of the input size .

