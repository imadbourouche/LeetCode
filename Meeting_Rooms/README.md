## Meeting Rooms

Given a list of meeting time intervals, determine if a single person can attend all meetings without overlaps.

Each interval has:

* `start`: meeting start time
* `end`: meeting end time

Return `true` if no meetings overlap, otherwise `false`.

### 💡 Approach

1. **Sort intervals by start time**.
2. **Scan sequentially** and compare each meeting with the next one.
3. If the current meeting ends **after** the next one starts → overlap detected.

This works because sorting guarantees only adjacent intervals need comparison.

### ⏱️ Complexity

* **Time:** `O(n log n)` (sorting)
* **Space:** `O(1)` (in-place sort)
