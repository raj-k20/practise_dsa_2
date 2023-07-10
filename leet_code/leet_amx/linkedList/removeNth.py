class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) ->ListNode:
        counter = 0
        prev = head
        curr = head.next
        if not curr:
            return head
        while curr:
            tmp = curr.next
            counter += 1
            if counter == n:
                prev.next = tmp
                del curr
            prev = prev.next
            curr = tmp
        return head

    def removeNthFromEnd_2(self, head: ListNode, n: int) ->ListNode:
        dummy = ListNode(0,head)
        left = dummy
        right = head
        while n > 0:
            right = right.next
            n-=1

        while right:
            left= left.next
            right = right.next

        left.next = left.next.next
        return dummy.next



lis = ListNode(1)
lis.next = ListNode(2)
lis.next.next = ListNode(3)
lis.next.next.next = ListNode(4)
lis.next.next.next.next = ListNode(5)

sol = Solution()
a = sol.removeNthFromEnd(lis,3)

while a:
    print(a.val,end='->')
    a=a.next
