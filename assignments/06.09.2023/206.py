class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse_list=None
        current=head
        while current:
            next_node = current.next
            current.next = reverse_list
            reverse_list = current
            current = next_node
        return reverse_list