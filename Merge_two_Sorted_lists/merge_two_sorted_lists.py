# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        head_res = None
        if list1.val < list2.val:
            head_res = list1
            list1 = list1.next
        else:
            head_res = list2
            list2 = list2.next
        tmp_head = head_res
        while list1 and list2:
            if list1.val < list2.val:
                tmp_head.next = list1
                list1 = list1.next
            else:
                tmp_head.next = list2
                list2 = list2.next
            tmp_head = tmp_head.next   
        tmp_head.next = list1 or list2
        return head_res

input1 = ListNode(1, ListNode(2, ListNode(4)))
input2 = ListNode(1, ListNode(3, ListNode(4)))
sol = Solution()
merged_list = sol.mergeTwoLists(input1, input2)
while merged_list:
    print(merged_list.val)
    merged_list = merged_list.next