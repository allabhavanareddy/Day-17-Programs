'''1290. Convert Binary Number in a Linked List to Integer'''

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s=""
        curr=head
        while(curr):
            s+=str(curr.val) #storing val as string
            curr=curr.next
        return int(s,2)



