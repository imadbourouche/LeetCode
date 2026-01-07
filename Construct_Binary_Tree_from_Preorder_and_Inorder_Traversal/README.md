# Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

## Traversal Properties:

* **Preorder:** `[Root -> Left Subtree -> Right Subtree]`
* The first element is always the **Root**.


* **Inorder:** `[Left Subtree -> Root -> Right Subtree]`
* Elements to the left of the Root belong to the **Left Subtree**.
* Elements to the right of the Root belong to the **Right Subtree**.


## Approach (recursion).

1. **Identify the Root:** The first element of the `preorder` list is the root of the current (sub)tree.
2. **Locate Root in Inorder:** We find the index of this root in the `inorder` list.
3. **Split the Lists:** * Everything to the left of that index in the `inorder` list forms the left subtree.
* Everything to the right forms the right subtree.
* We slice the `preorder` list accordingly based on the size of these subtrees.

4. **Recursive Step:** Repeat the process for the left and right children until the lists are empty (base case).

## Complexity



* **Time Complexity:** 

* Worst case: O(n²)
    * inorder.index(...) is O(n) at each recursive call
    * List slicing (preorder[...], inorder[...]) is also O(n)
* Happens for skewed trees.
* *Optimization Tip:* Using a hash map to store `inorder` indices can reduce this to .


* **Space Complexity:** 
* O(n) due to recursion
* O(n2) This is due to the creation of new list slices at each recursive call.
* *Optimization Tip:* Passing index pointers instead of slices can reduce space.
