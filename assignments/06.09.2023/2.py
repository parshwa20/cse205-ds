class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        carry = 0
        while l1!=None or l2!=None or carry!=0:
            l1value = l1.val if l1 else 0
            l2value = l2.val if l2 else 0
            total = l1value + l2value + carry
            current.next = ListNode(total%10)
            carry = total//10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            current = current.next
        return head.next