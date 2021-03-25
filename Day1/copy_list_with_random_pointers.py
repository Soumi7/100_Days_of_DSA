"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        i = head
        while(i!=None):
            front = i.next
            copy = Node(i.val)
            i.next = copy
            copy.next = front
            i = front
            
        i = head
        while(i!=None):
            if i.random!=None :
                i.next.random = i.random.next
            i=i.next.next
            
        pseudo_head = Node(0)
        i = head
        copy = pseudo_head
        while(i!=None):
            front = i.next.next
            copy.next = i.next
            i.next = front
            copy = copy.next
            i = i.next
        return(pseudo_head.next)
            
        
