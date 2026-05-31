# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        single = head
        double = head

        while single and double:
            single = single.next
            double = double.next
            if double is not None:
                double = double.next
            else:
                return False
            
            if single is double:
                return True
            
        return False