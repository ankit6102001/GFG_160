
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        if not head or k == 0:  
            return head

        temp = head
        length = 1
    
        while temp.next:
            temp = temp.next
            length += 1
        temp.next = head  
    
        k = k % length  
        if k == 0:      
            temp.next = None
            return head
    
        steps_to_new_tail =  k  
        new_tail = head
    
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
    
        new_head = new_tail.next  
        new_tail.next = None      
    
        return new_head 
