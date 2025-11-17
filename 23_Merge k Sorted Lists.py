# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            merged_list = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else []
                merge_l1_l2 = self.merge_lists(l1, l2)
                merged_list.append(merge_l1_l2)

            lists = merged_list

        return lists[0]

    def merge_lists(self, l1: List[ListNode], l2: List[ListNode]) -> List[ListNode]:

        dummy_head = ListNode()
        curr = dummy_head

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next
        while l1:
            curr.next = l1
            l1 = l1.next
            curr = curr.next
        while l2:
            curr.next = l2
            l2 = l2.next
            curr = curr.next

        return dummy_head.next
