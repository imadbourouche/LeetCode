## Top K Frequent Elements
Given a non-empty array of integers, return the k most frequent elements.

### Approach (Bucket Sort)
1. Create a frequency map to count the occurrences of each element in the array.
2. Create an reverse frequency map, where the key represents the frequency and each value contains a list of elements with that frequency.
3. Iterate through the reverse frequency map from the highest frequency to the lowest, collecting elements until k elements are collected.

### Complexity
* **Time:** O(n) — counting frequencies and collecting top k elements.
* **Space:** O(n) — storing frequencies in maps.

### Key Idea
Using a bucket sort approach allows grouping elements by their frequencies, enabling efficient retrieval of the top k frequent elements without the need for sorting the entire array.