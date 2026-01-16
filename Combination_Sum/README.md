# Combination Sum – Backtracking Solution

Given a list of distinct integers `candidates` and a target integer `target`, return all unique combinations where the chosen numbers sum to `target`.
Each number may be used **unlimited times**.

## Approach

We explore the solution space using **depth-first search with backtracking**.

At any point, the state is defined by:

* `i` → current index in `candidates`
* `sum_result` → current sum
* `sol` → current combination being built

### Decision at Each Step

For a candidate at index `i`, we have **two choices**:

#### 1 Take `candidates[i]`

* Add it to `sol`
* Increase `sum_result`
* **Stay at the same index `i`**
  → allows unlimited reuse of the same number

#### 2 Skip `candidates[i]`

* Do not add it
* Move to `i + 1`
  → try the next candidate

### Stopping Conditions (Pruning)

We stop recursion early when:

* `sum_result == target`
  → valid combination found, store a copy
* `sum_result > target`
  → invalid path, stop
* `i >= len(candidates)`
  → no more numbers to try

This pruning avoids unnecessary work.


### Why This Works

* Guarantees all valid combinations are explored
* No duplicates (indices only move forward)
* Efficient due to early pruning

## Complexity

* **Time:** O(N**T) where N is the number of candidates and T is the number of candidates
* **Space:** `O(target)` recursion depth (worst case)
