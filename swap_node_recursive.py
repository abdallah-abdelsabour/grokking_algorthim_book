# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head==None or head.next ==None:
            return head
        
        p1 = head
        p2 = p1.next
        p3 = p2.next 
        
        p1.next = p3
        p2.next  = p1
        
        if p3 != None:
            
            p1.next = self.swapPairs(p3)
            
        return p2

            
                
                
                
                
               