# Trie (Prefix Tree) in Python

A simple and efficient implementation of a **Trie** (also called a Prefix Tree) that supports word insertion, full-word search, and prefix search.

All operations run in **O(n)** time where `n` is the length of the input string.

## Data Structure

Each node contains:
- `children`: dictionary mapping characters to child nodes
- `end_of_word`: marks if a complete word ends here

## API

### `insert(word: str) -> None`
Adds a word to the trie.

### `search(word: str) -> bool`
Returns `true` if the word exists in the trie.

### `startsWith(prefix: str) -> bool`
Returns `true` if any word in the trie starts with the given prefix.

## Complexity

* Time complexity 

| Operation | Time |
| --------- | ---- |
| Insert    | O(n) |
| Search    | O(n) |
| Prefix    | O(n) |

* Space complexity is **O(total characters inserted)**.
