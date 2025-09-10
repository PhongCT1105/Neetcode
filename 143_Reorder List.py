# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head or not head.next:
            return 

        sp, fp = head, head

        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next

        # Reverse the second half
        second = sp.next
        sp.next = None
        prev = None
        curr = second
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        second = prev
        first = head

        while second:
            m1, m2 = first.next, second.next
            first.next = second
            second.next = m1

            first = m1
            second = m2                    

