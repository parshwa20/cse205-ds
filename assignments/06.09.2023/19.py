class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count=0
        while temp:
            count+=1
            temp=temp.next
        
        point = count - n -1
        count=0
        temp=head

        if point == -1:
            return head.next
        
        while temp:
            if count==point:
                temp.next = temp.next.next
                break
            temp = temp.next
            count+=1
        return head