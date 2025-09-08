# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        sp, fp = head, head

        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next

        prev = None
        curr = sp

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
                
        curr_r = prev
        curr_l = head
        res = 0

        while curr_r:
            total = curr_r.val + curr_l.val
            if res < total:
                res = total

            curr_r = curr_r.next
            curr_l = curr_l.next

        return res
