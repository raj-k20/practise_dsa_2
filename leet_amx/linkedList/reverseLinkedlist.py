# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseList(self, head: ListNode):
        curr , prev =  head, None

        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

lis = ListNode(1)
lis.next = ListNode(2)
lis.next.next = ListNode(3)

sol = Solution()
print(sol.reverseList(lis).val)

