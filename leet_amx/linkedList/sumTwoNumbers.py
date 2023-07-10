# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1+v2+carry
            carry = (val)//10
            val = val % 10
            cur.next = ListNode(val)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return cur.next


lis = ListNode(2)
lis.next = ListNode(4)
lis.next.next = ListNode(3)
#lis.next.next.next = ListNode(4)
#lis.next.next.next.next = ListNode(5)


lis2 = ListNode(5)
lis2.next = ListNode(6)
lis2.next.next = ListNode(4)
sol = Solution()
a = sol.addTwoNumbers(lis,lis2)

