# Median Finder (Data Stream)

Finding the median in a sorted list is easy (), but maintaining that median as new numbers are constantly added can be expensive if we re-sort the list every time ( or ).

This solution allows us to:

1. **Add a number** in  time.
2. **Find the median** in  time.


##  The Algorithm: Two Heaps

The solution uses two priority queues (heaps) to divide the numbers into two halves:

1. **Small Heap (Max-Heap):** Stores the smaller half of the numbers. The largest number in this half is at the top.
2. **Large Heap (Min-Heap):** Stores the larger half of the numbers. The smallest number in this half is at the top.

### How it works:

* **Balance:** We ensure the size difference between the two heaps is never more than 1.
* **Ordering:** Every element in the `small` heap is  every element in the `large` heap.
* **Calculation:** * If the heaps are equal in size, the median is the average of the two tops.
* If one heap is larger, the median is the top of that specific heap.

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
| --- | --- | --- |
| `addNum` | O(log n) | O(1) |
| `findMedian` | O(1) | O(1) |
| **Total** | O(n log n) | O(n) |

## Implementation Details

* **Python's `heapq`:** Since `heapq` only provides a min-heap, we store numbers in the `small` heap as **negative** values to simulate a max-heap behavior.
* **Rebalancing:** The code automatically detects when one side becomes too heavy and "shuffles" an element to the other side to maintain the  lookup property.
