from typing import List, Optional
# Definition for singly-linked list.
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


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        head = lists[0]
        for i in range(1, len(lists)): # O(k)
            head = self.mergeTwoLists(head, lists[i]) # O(N) where N is total number of nodes
        return head

input1 = ListNode(1, ListNode(4, ListNode(5)))
input2 = ListNode(1, ListNode(3, ListNode(4)))
input3 = ListNode(2, ListNode(6))
sol = Solution()
merged_list = sol.mergeKLists([input1, input2, input3]) # O(k * N) space O(1)
while merged_list:
    print(merged_list.val)
    merged_list = merged_list.next