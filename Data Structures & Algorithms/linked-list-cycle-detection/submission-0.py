# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first, after = head, head

        while after and after.next:
            first = first.next
            after = after.next.next
            if first == after:
                return True
        return False