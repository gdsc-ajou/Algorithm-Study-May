# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        left = []
        while fast.next and fast.next.next:
            left.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        if fast.next:
            left.append(slow.val)

        slow = slow.next
        while slow:
            if left.pop() != slow.val:
                return False
            slow = slow.next
        
        return True
        
