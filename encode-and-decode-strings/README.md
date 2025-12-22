# String Encode/Decode

My solution for **encode a list of strings into a single string** and **decode it back** safely, even if the strings contain characters that could interfere with parsing.

### `encode(strs: List[str]) -> str`

* Converts a list of strings into a single string.
* Escapes commas in the original strings by prefixing them with a backslash (`\,`).
* Joins all strings with commas as separators.

### `decode(s: str) -> List[str]`

* Converts an encoded string back into the original list of strings.
* Handles escaped commas correctly.
* Iterates through the string, reconstructing each original string.

## Complexity

* **Time:** O(m), where m is the total length of all strings.
* **Space:** O(m) for the output string/list.