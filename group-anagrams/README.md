## Group Anagrams Solution

This solution groups words that are **anagrams of each other**.

### How it works

1. Create an empty dictionary `anagram_dict`.
2. For each string `s` in the list:

   * Sort the characters in `s` to create a `key`.
   * Use the `key` in the dictionary:

     * If the key exists → append `s` to its list.
     * If not → create a new list with `s`.
3. Convert all dictionary values to a list and return.

### Complexity

* **Time:** O(n * k log k)

  * `n` = number of strings, `k` = max string length (sorting each string)
* **Space:** O(n) — for storing the groups in the dictionary

### Key Idea

Sorting each string gives a **unique identifier** for its anagram group, allowing efficient grouping using a hash map.
