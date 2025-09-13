# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        left = 0
        head = ListNode()
        curr = head

        while l1 or l2:
            val = 0
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            val += left
            left = 0
            if val >= 10:
                left = 1
                val -= 10

            node = ListNode(val)
            curr.next = node
            curr = curr.next

        if left == 1:
            node = ListNode(1)
            curr.next = node

        return head.next
