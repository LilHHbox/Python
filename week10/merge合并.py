# Author: Lilbox
# Time:2022/1/10 12:19


# def mergeNull(list1,list2,list3,num2):
#     for i in range(num2):
#         list3.append(list2[i])
#     return list3
# def mergeTwoList(list1,list2,list3):
#     num1 = len(list1)
#     num2 = len(list2)
#     if list1 and list2:
#         if list1[0]<=list2[0]:
#             list3.append(list1[0])
#             list1.pop(0)
#             mergeTwoList(list1,list2,list3)
#         else:
#            list3.append(list2[0])
#            list2.pop(0)
#            mergeTwoList(list1, list2,list3)
#     elif not list1 and list2:
#            list3=mergeNull(list1,list2,list3,num2)
#            return list3
#     elif not list2 and list1:
#            list3 = mergeNull(list2,list1,list3, num1)
#            return list3
#     else:
#            return list3

def mergeNull(list2,list3):
    while  list2:
        list3.append(list2[0])
        list2.pop(0)
    return list3
def mergeTwoList(list1,list2):
    if list1 and list2:
        if list1[0]<=list2[0]:
            l3.append(list1[0])
            list1.pop(0)
            mergeTwoList(list1,list2)
        else:
           l3.append(list2[0])
           list2.pop(0)
           mergeTwoList(list1, list2)
    elif not list1 and list2:
           return mergeNull(list2,l3)
    elif not list2 and list1:
           return mergeNull(list1,l3)
    else:
           return l3

l3=[]
l1=[1,2]
l2=[1,2]
mergeTwoList(l1,l2)
print(l3)




#官方：
#法1
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
#法2
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = l1 if l1 is not None else l2

        return prehead.next




#
# def mergeNull(list1,list2,num2):
#     for i in range(num2):
#         list1.append(list2[i])
#     return list1
# def mergeTwoList(list1,list2):
#     if list1 and list2 and num1!=0:
#         if list1[0]<=list2[0]:
#             list1.append(list1[0])
#             list1.pop(0)
#             num1-=1
#             mergeTwoList(list1,list2)
#         else:
#            list1.append(list2[0])
#            list2.pop(0)
#            mergeTwoList(list1, list2)
#     elif num1==0 and list2:
#            list1=mergeNull(list1,list2,num2)
#            return list1
#     elif not list2 and list1:
#            list1 = mergeNull(list2,list1, num1)
#            return list1
#     else:
#            return list1

