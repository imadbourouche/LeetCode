# Best Time to Buy and Sell Stock

## Overview

This solution finds the **maximum profit** from a single buy and a single sell of a stock, given daily prices.

## Approach

* Track the **minimum price so far** while iterating.
* For each day:

  * Update the minimum price if a lower price is found.
  * Otherwise, compute the profit if sold today and update the maximum profit.

## Complexity

* **Time:** `O(n)` — single pass through prices
* **Space:** `O(1)` — constant extra space

