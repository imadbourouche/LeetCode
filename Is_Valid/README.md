# Is Valid Parentheses
Description: Determine if the input string of parentheses is valid. A string is valid if all types of parentheses are correctly opened and closed in the right order.

## Solution using stack
* Define a function `isValid` that takes a string `s` as input.
* Initialize an empty list `stack` to keep track of opening parentheses.
* Iterate through each character `i` in the string `s`:
  - If `i` is an opening parenthesis (`(`, `{`, `[`), append it to `stack`.
  - If `i` is a closing parenthesis (`)`, `}`, `]`):
    - Check if `stack` is empty. If it is, return `False` (indicating an unmatched closing parenthesis).
    - Pop the last element from `stack` and check if it matches the corresponding opening parenthesis for `i`. If it doesn't match, return `False`.
* If `stack` is not empty after processing all characters, return `False`.
* Otherwise, return `True`.

## Complexity 
- Time Complexity
    * O(n), where n is the length of the string `s`. Each character is processed once.

- Space Complexity
    * O(n) in the worst case, where all characters are opening parentheses and stored in the stack.

