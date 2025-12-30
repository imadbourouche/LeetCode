
# Lowest Common Ancestor in a Binary Search Tree

Given a **Binary Search Tree (BST)** and two nodes `p` and `q`, find their **Lowest Common Ancestor (LCA)**.

**LCA** = the closest node that is a parent of both `p` and `q`.

## Key BST Property

In a BST:

* Left subtree values `< node value`
* Right subtree values `> node value`


## Iterative Approach

### Algorithm

1. Start from the root
2. While the current node exists:

   * If both `p` and `q` are greater → move right
   * If both `p` and `q` are smaller → move left
   * Else → current node is the LCA


### Complexity (Iterative)

* **Time:** `O(h)`
* **Space:** `O(1)`


### Complexity (Recursive)

* **Time:** `O(h)`
* **Space:** `O(h)`