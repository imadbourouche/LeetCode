# Climbing Stairs Solution

**LeetCode problem: [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)**

You are climbing a staircase. It takes `n` steps to reach the top. Each time you can either climb **1 step** or **2 steps**. Find out **how many distinct ways** you can climb to the top.

## Approach (recursion with memoization)

* Use **recursive function** `recv(current)` to explore all possible paths (a decision tree).
* **Memoization** with a global map `memo` to store results of subproblems and avoid redundant computation.
* **Base cases**:
  * If `current == N`, return 1 (we found a solution or a path).
  * If `current > N`, return 0 (the path will not lead to a solution).

* **Recursive step**: sum the results of taking 1 step or 2 steps: `recv(current + 1) + recv(current + 2)`

## Complexity

* **Time Complexity:** `O(n)` – each step from `0` to `N` is computed once (without memoziation it will be `O(2^n)`).
* **Space Complexity:** `O(n)` – recursion stack + memoization map.
