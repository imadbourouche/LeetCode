# Word Search – Backtracking Solution

Given a 2D grid of characters and a target word, determine if the word exists in the grid.

Rules:

* The word must be constructed from sequentially adjacent cells.
* Adjacent cells are **horizontally or vertically** neighboring.
* Each cell can be used **only once** per word search.

## Approach

This solution uses **Depth-First Search (DFS) with Backtracking**.

* Start a DFS from each cell.
* At each step:

  * Check boundaries.
  * Match the current character with the word.
  * Mark the cell as visited (`*`) to avoid reuse.
  * Explore all 4 directions.
  * Restore the cell after exploring (backtrack).

This ensures correctness while keeping the grid unchanged after the search.

## Complexity

| Metric | Value                                                 |
| ------ | ----------------------------------------------------- |
| Time   | **O(ROWS × COLS × 4^L)** where L = length of the word |
| Space  | **O(L)** recursion stack                              |

Worst case occurs when every cell is explored for each letter.

