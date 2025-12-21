## Two Sum Solution

This solution solves the **Two Sum** problem using a **hash map** for efficient lookup.

### Approach

1. Iterate through the array `nums`.
2. For each number:
    * Check if we already saw a number that would add up with it to reach the target.
        * If yes → return the two indices.
    * If not → compute `difference = target - current_element` and store it in `solutions` with the current index of the number that we need (i.e `current_element`).

3. If no such pair is found, return an empty list.

### Complexity

* **Time:** O(n) — each element is visited once.
* **Space:** O(n) — stores differences in a dictionary.

### Key Idea

Using a hash map allows **instant lookup** for the complement, avoiding the need for nested loops.