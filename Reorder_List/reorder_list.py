from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        tmp = head
        while tmp:
            stack.append(tmp)
            tmp = tmp.next
        
        tmp = head
        if not stack:
            return head
        v = stack.pop()
        while (v != tmp) and (v != tmp.next):
            v.next = tmp.next
            tmp.next = v
            tmp = v.next
            v = stack.pop()
        if v == tmp:
            tmp.next = None
        elif v == tmp.next:
            tmp.next.next = None
        return head

input = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
sol = Solution().reorderList(input)
while sol:
    print(sol.val)
    sol = sol.next

