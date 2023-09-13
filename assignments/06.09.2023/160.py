class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l = []
        while headA:
            l.append(headA)
            headA = headA.next
        while headB:
            if headB in l:
                return headB
            headB = headB.next
        return None