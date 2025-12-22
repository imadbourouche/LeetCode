# Product of Array Except Self

This solution computes the **product of all elements in an array except the current element** without using division.

## Approach

1. **Left product pass:**

   * `arr1[i]` stores the product of all elements to the **left** of `i`.
   * Initialize `arr1[0] = 1` and accumulate products from left to right.

2. **Right product pass:**

   * Use a temporary variable `tmp` to store the product of elements to the **right**.
   * Multiply `tmp` with the left products in `arr1` while iterating from right to left.

3. **Result:**

   * `arr1[i]` contains the product of all elements **except `nums[i]`**.


## Complexity

* **Time:** O(n), two linear passes over the array.
* **Space:** O(n), storing the result in `arr1`.