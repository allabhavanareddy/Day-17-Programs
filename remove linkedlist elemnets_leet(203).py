'''203. Remove Linked List Elements
Given the head of a linked list and an integer val, remove all the
nodes of the linked list thathas Node.val == val, and return the
new head.
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]'''

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        front=ListNode()
        front.next=head
        curr=front
        prev=None
        while(curr!=None):
            if(curr.val==val):
                if(prev!=None):
                    prev.next=prev.next.next
                    curr=prev
                else:
                    prev=None
            prev=curr
            curr=curr.next
        return front.next
