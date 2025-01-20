'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
class Solution:
    def sortedMerge(self, head1, head2):
        if not head1:
            return head2
        if not head2:
            return head1

        if head1.data < head2.data:
            new_head = head1
            head1 = head1.next
        else:
            new_head = head2
            head2 = head2.next
        
        temp = new_head
        
        while head1 and head2:
            if head1.data < head2.data:
                temp.next = head1
                head1 = head1.next
            else:
                temp.next = head2
                head2 = head2.next
            temp = temp.next
        
        if head1:
            temp.next = head1
        elif head2:
            temp.next = head2
        
        return new_head
        

