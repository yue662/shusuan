# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        out=ListNode(0)
        outs=out
        while list1 and list2:
            if list1.val<=list2.val:
                outs.next=list1
                list1=list1.next
            else:
                outs.next=list2
                list2=list2.next
            outs=outs.next
        if list1:
            outs.next=list1
        if list2:
            outs.next=list2
        return out.next