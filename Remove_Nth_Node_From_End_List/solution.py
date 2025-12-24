# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # One pass solution
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fp = head
        sp = head
        while n > 0:
            sp = sp.next
            n -= 1
        prev = head
        while sp:
            sp = sp.next
            prev = fp
            fp = fp.next
        if fp == head:
            head = prev.next
        else:
            prev.next = fp.next
        return head

    # Two pass solution
    def removeNthFromEnd_two_pass(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        tmp = head
        while tmp:
            size += 1
            tmp = tmp.next
        index_to_remove = (size - n) + 1
        tmp = head
        prev = None
        i = 0
        while tmp:
            i += 1
            if index_to_remove == i:
                if size == 1:
                    return None
                if i == 1:
                    head = head.next
                else:
                    prev.next = tmp.next
                return head
            prev = tmp
            tmp = tmp.next
        return head 