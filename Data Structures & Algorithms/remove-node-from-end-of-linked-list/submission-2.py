# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Including dummy node to ensure distance of n between left & right node
        dummy = ListNode(0,head)
        left = dummy
        right = head
        # Keeping right pointer and left pointer apart by n distance
        while n>0:
            right = right.next
            n -=1
        
        while right:
            left = left.next
            right = right.next
        # Deleting the nth node from last by updating the next value of left to the value after the last n node
        left.next = left.next.next
        return dummy.next
        