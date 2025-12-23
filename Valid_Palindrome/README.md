# Valid Palindrome
 This solution checks if a given string is a valid palindrome, considering only alphanumeric characters and ignoring cases.

## Approach
The approach involves:
1. Removing all non-alphanumeric characters from the string.
2. Converting the string to lowercase.
3. Using two pointers (left and right) to compare characters from both ends of the string.
4. If any pair of characters does not match, return False; otherwise, return True.

## Complexity Analysis
* **Time Complexity:** O(n)
    * We traverse the string a constant number of times (for cleaning and for checking), leading to linear time complexity.
* **Space Complexity:** O(n)
    * We use additional space to store the cleaned version of the string.