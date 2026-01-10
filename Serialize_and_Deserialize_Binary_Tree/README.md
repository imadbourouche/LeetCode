# Binary Tree Serializer & Deserializer

Solution for converting a binary tree into a string representation (**Serialization**) and converting that string back into the original tree structure (**Deserialization**).

## Approach (Level Order Traversal (BFS))

### 1. Serialization (Tree to String)

The algorithm uses a `deque` to perform a level-order traversal. For every node encountered:

1. It appends the direction tag (`L` or `R`) and the node's value to the result string.
2. If a child is `None`, it records `-`.
3. A `#` is appended after every right child to mark the completion of a sibling pair.

**Example Format:** `r1L2R3#L-R-L-R-#`

### 2. Deserialization (String to Tree)

The process is reversed using a queue to reconstruct the tree level by level:

1. **Root Extraction**: Finds the first `L` to determine where the root value ends.
2. **Breadth-First Reconstruction**: For each node in the queue, it searches for the corresponding `L...R...#` block in the string to attach the left and right children.

## Complexity Analysis

### **Serialization (`serialize`)**

* **Time Complexity:** `O(n)`

  * Each node is visited **once** in a BFS traversal.
  * Appending to the result string is linear in the number of nodes.
* **Space Complexity:** `O(n)`

  * BFS queue stores nodes level by level (up to `O(n)` in the worst case).
  * Result string also grows linearly with the number of nodes.

### **Deserialization (`deserialize`)**

* **Time Complexity:** `O(n)`
  * Each node in the serialized string is processed exactly once.
  * String slicing and `find` operations are bounded by the total string length (linear in number of nodes).
* **Space Complexity:** `O(n)`
  * Queue stores nodes during reconstruction (up to `O(n)`).
  * Constructed tree has `n` nodes.
