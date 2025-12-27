# Minimum Window Substring

## Problem Description

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum window substring** of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

## Approach: Sliding Window

The solution uses a **two-pointer (Sliding Window)** approach to find the optimal window in  time.

### How it works:

1. **Frequency Maps:** We first create a frequency map `count_t` of the target string `t` and `need` variable to store the number of unique characters in `t` that we need to find.
2. **Initialize Pointers and Counters:** We initialize two pointers `l` and `r` to represent the current window in `s`, a `have` counter to track how many unique characters from `t` are currently in the window, and a `window_counts` dictionary to store the frequency of characters in the current window.
3. **Expand (Right Pointer):** We move the `r` pointer to the right, adding characters to our current `window_counts`. If a character's frequency matches its frequency in `t`, we increment our `have` counter.
4. **Contract (Left Pointer):** Once `have == need` (meaning all required characters are present), we try to shrink the window from the left (`l`) to find the smallest possible valid substring.
5. **Update Result:** During the contraction phase, we update the `minimum_window` whenever we find a smaller length.
6. **Repeat:** We continue expanding and contracting until the right pointer reaches the end of string `s`.

## Complexity Analysis
- **Time Complexity**: O(m + n) we visit each character in `s` and `t` at most twice.
- **Space Complexity**: O(k) where K is the number of unique characters in t. Because the code checks if s[r] in count_t, the window_counts dictionary only stores relevant characters.