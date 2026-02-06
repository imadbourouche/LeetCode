## Insert Interval

Given a list of **non-overlapping, sorted intervals** and a **new interval**, insert the new interval into the list **merging overlapping intervals** if necessary.
Return the resulting list of intervals in sorted order.

### Approach

1. Add intervals completely before `newInterval`.
   * Any interval with `end < newInterval.start` goes directly to the result.

2. If we are in the end of the intervals we add just the `newInterval` to the result and return.

3. update the `newInterval[0]` to be the minimum of the newInterval[0] and the current interval's start, because they overlap

3. Merge overlapping intervals.

   * Continue the loop to find the end of the newInterval 
   * Update `newInterval[1]` to the maximum end of overlapping intervals each time.

4. Merge the `newInterval` with the result list.

5. Add intervals completely after `newInterval`.
   * Any interval with `start > newInterval.end` goes directly to the result.

### Complexity

* **Time:** `O(n)` — each interval is processed once.
* **Space:** `O(n)` — result list stores all intervals.
