# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
            dumy = ListNode(val =0,next = head )
            
            prev , curr = dumy ,head
            
            while curr and curr.next :
                
                nxt_pair = curr.next.next
                second = curr.next 
                
                prev.next = second 
                second.next = curr
                curr.next = nxt_pair
                
                 
                prev = curr
                curr = nxt_pair
                
            return dumy.next    
                
                
                
                
                
               