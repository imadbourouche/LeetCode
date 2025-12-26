# Longest Substring Without Repeating Characters

This solution finds the length of the longest substring without repeating characters in a given string `s`.

## Approach

* Use a sliding window with two pointers: `l` (left) and `r` (right).
* Maintain a dictionary `map_li` to store the latest index of each character.
* Move `r` to expand the window.
* **Key detail:** If `s[r]` is already in `map_li` but its last index is less than `l`, it means the character occurred **outside the current window**, so we just update its index and continue expanding. Otherwise, move `l` past the previous occurrence to avoid duplicates.
* Continuously update `longest` with the current window size `r - l`.

### Complexity

* **Time:** O(n) each character is processed at most twice.
* **Space:** O(min(n, charset)) — dictionary stores indices for unique characters.