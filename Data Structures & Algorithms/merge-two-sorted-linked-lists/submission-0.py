# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1, temp2 = list1, list2
        ret = ListNode()
        dummy = ret
        while temp1 and temp2:
            if temp1.val < temp2.val:
                ret.next = temp1
                temp1 = temp1.next
                ret = ret.next
            else:
                ret.next = temp2
                temp2 = temp2.next
                ret = ret.next
        if temp1:
            ret.next = temp1
        else:
            ret.next = temp2
        return dummy.next