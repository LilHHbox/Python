# Author: Lilbox
# Time:2022/1/17 13:52

# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         if l1 is None:
#             return l2
#         elif l2 is None:
#             return l1
#         elif l1.val < l2.val:
#             l1.next = self.mergeTwoLists(l1.next, l2)
#             return l1
#         else:
#             l2.next = self.mergeTwoLists(l1, l2.next)
#             return l2


class ListNode:
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next
from re import A
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if head.next==None:
            return head
        note1=head
        note2=head.next
        x=0
        while note2.next!=None:
             x=note1.val
             if x==note2.val:
                if not note2.next:
                    note1.next=None
                else:
                    note1.next=note2.next
                    note2=note2.next
             else:
                 note1=note1.next
                 note2=note1.next
        return head
lis=[1,2,3,3]
Solution.deleteDuplicates(lis)
print(lis)
