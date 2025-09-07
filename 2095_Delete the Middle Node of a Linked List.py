# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getLength(self, head) -> int:
        curr = head
        length = 0

        while curr:
            length += 1
            curr = curr.next
        
        return length

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        middle = self.getLength(head) // 2

        curr = head

        while middle >= 2:
            curr = curr.next
            middle -= 1
        

        curr.next = curr.next.next
        
        return head
        
