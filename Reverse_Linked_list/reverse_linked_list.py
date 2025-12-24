# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        while head:
            tmp_head = head.next
            head.next = previous
            previous = head
            head = tmp_head
        return previous

input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol = Solution()
reversed_list = sol.reverseList(input)
while reversed_list:
    print(reversed_list.val)
    reversed_list = reversed_list.next