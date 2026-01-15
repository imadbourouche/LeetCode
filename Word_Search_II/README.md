# Word Search II Solution

Given an `m x n` board of characters and a list of strings `words`, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where **adjacent** cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

## Technical Approach

This solution utilizes a combination of a **Trie (Prefix Tree)** and **Backtracking (DFS)** to efficiently search for multiple words that shared the same prefix simultaneously.

### 1. The Trie Data Structure

Instead of searching for each word individually, we store all target words in a Trie. This allows us to:
* Prune the search space: If a prefix does not exist in our Trie, we stop searching that path immediately.
* Identify multiple words that share common prefixes in a single pass over the board.

### 2. Backtracking with DFS

We iterate through every cell in the grid and initiate a Depth-First Search (DFS) if the character at that cell exists as a starting character in our Trie.

* **Marking Visited Cells:** To ensure we don't reuse the same cell in a single word, we temporarily replace the character with an asterisk `*`.
* **check word**: if the node has end_of_word true, that means we are in the end of a word and we will add the word in the list of result.
* **Exploration:** else we continue exploring all four directions (Up, Down, Left, Right).
* **Backtracking:** After the recursive calls return, we restore the original character to the board to allow other paths to use it.

## Complexity Analysis

**Time Complexity**: 
    * O(R * C * (4 * 3^L-1)):  R * C is the number of cells in the board and  L is the maximum length of a word. We explore 4 directions initially and up to 3 directions thereafter.
**Space Complexity**:
    * O(M * L):  is the total number of words and  is the average length of the words stored in the Trie.