# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, head1: ListNode, head2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        curr = dummy

        while head1 is not None and head2 is not None:
            if head1.val <= head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next

        if head1 is not None:
            curr.next = head1
        else:
            curr.next = head2
        
        return dummy.next
        