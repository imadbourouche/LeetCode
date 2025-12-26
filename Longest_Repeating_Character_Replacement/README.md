# Longest Repeating Character Replacement

This solution finds the length of the longest substring in a string `s` where you can replace at most `k` characters to make all characters in the substring the same.

## Approach

* Use a **sliding window** with pointers `l` (left) and `r` (right).
* Maintain a dictionary `freq_map` to count character frequencies in the current window.
* Track `most_frequent` as the **highest frequency character in the current window**, updated each time the window changes
* If the number of characters that need replacement `(window_length - most_frequent)` exceeds `k` where `window_length = r - l + 1`, shrink the window from the left by decreasing `freq_map[s[l]]` and moving `l` forward.
* Continuously update `longest` with the size of the valid window.

## Complexity

* **Time:** O(n) — n is the length of `s`, Since the alphabet size is at most 26 characters, computing `max(freq_map.values())` is effectively **O(1)**, making this solution practically linear in the length of the string.
* **Space:** O(1) — stores counts for up to 26 characters in the window.

