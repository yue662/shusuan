# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        sl=[]
        while head:
            sl.append(int(head.val))
            head=head.next
        check=True
        for i in range(len(sl)//2):
            if sl[i]!=sl[-i-1]:
                check=False
                break
        return check