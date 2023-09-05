class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        while current and current.next:
            head=head.next
            current=current.next.next
        return head