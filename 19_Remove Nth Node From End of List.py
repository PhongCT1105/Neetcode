# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Reverse Linked List  
        if not head or not head.next:
            return 
        
        curr = head
        prev = None
        length = 1
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        dumphead = prev
        prev = None
        curr = dumphead

        while curr and n > 2:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            n -= 1
        
        if not n == 1:
            curr.next = curr.next.next
        else:
            curr = curr.next

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt  

        return prev
