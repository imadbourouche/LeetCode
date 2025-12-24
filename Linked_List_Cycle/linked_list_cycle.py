# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next

class Solution:
    # Modifies node values to mark visited nodes
    def hasCycle_with_marking(self, head: Optional[ListNode]) -> bool:
        while head and head.next:
            if head.val == None:
                return True
            head.val = None
            head = head.next
        return False
    
    # Floyd’s Cycle Detection (Slow & Fast Pointers)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast= head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True            
        return False

input1 = ListNode(3, ListNode(2, ListNode(0, ListNode(4))))
input1.next.next.next = input1.next  # Create a cycle for testing
solution = Solution()
print(solution.hasCycle(input1))  # Expected output: True
print(solution.hasCycle_with_marking(input1))  # Expected output: True