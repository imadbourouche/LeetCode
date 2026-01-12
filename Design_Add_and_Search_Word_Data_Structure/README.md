# WordDictionary - LeetCode Solution

This repository contains a Python implementation of a **Word Dictionary** using a **Trie (Prefix Tree)**, designed to efficiently add words and search with support for the wildcard character `.`.

We have to implement a data structure that supports the following operations:

* `addWord(word)`: Adds a word to the data structure.
* `search(word)`: Searches for a word in the data structure. The word may contain the dot character `.` to represent any one letter.

## Approach

* **Data Structure**: Trie
  * Each node contains a dictionary of child nodes and a boolean `end_of_word` to mark the end of a word.

* **Adding a Word**:
  * Traverse through the characters of the word.
  * Create nodes if the character is not already present.
  * Mark the last node as `end_of_word = True`.

* **Searching a Word**:
  * Traverse nodes recursively.
  * If a `.` is encountered, recursively search all child nodes.
  * Return `True` if a valid path ends at `end_of_word`.

## Complexity

* **Time Complexity**:

  * `addWord`: O(n) where n is the length of the word
  * `search`: O(m * 26^k) in worst case (m = length of word, k = number of wildcards which equal to 2 in this problem)
* **Space Complexity**: O(Total characters added)
