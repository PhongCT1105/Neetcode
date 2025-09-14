# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
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

        curr1, curr2 = head, prev

        while curr1 and curr2:
            if curr1.val != curr2.val:
                return False

            curr1 = curr1.next
            curr2 = curr2.next

        return True
