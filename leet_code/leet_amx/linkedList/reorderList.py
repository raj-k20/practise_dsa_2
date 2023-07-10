class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast = head
        while fast:
            slow =slow.next
            fast = fast.next.next

        sec = slow.next
        prev = slow.next = None
        while slow:
            temp = sec
            sec.next = prev
            prev = sec
            slow = temp

        fir,sec = head,prev
        while sec:
            tmp1,tmp2= fir.next,sec.next
            fir.next = sec
            sec.next = tmp1
            fir,sec= tmp1,tmp2
