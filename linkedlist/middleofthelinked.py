# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        s, f = head, head

        while f != None and f.next != None:
            f = f.next.next
            s = s.next
        return head