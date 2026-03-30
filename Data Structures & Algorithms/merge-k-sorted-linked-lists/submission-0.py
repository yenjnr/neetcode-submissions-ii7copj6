# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        while True:
            check = -1
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if check == -1 or lists[check].val > lists[i].val:
                    check = i

            if check == -1:
                break
            curr.next = lists[check]
            lists[check] = lists[check].next
            curr = curr.next

        return dummy.next