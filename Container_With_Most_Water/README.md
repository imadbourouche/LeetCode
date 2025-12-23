# Container With Most Water – Solution

This Python solution finds the maximum water a container can store, given a list of heights representing vertical lines.

## Approach

* **Two-pointer technique:** Start with pointers at the beginning and end of the list.
* Calculate the current container area:
  - area = (right - left) * min(height[left], height[right])
* Move the pointer pointing to the shorter line inward, since the area is limited by the shorter line.
* Keep track of the maximum area seen so far.

## Complexity

* **Time:** O(n) – each pointer moves at most n steps.
* **Space:** O(1) – constant extra space.
