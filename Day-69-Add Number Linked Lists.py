''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
    
    def addTwoLists(self, num1, num2):
        num1 = self.reverseList(num1)
        num2 = self.reverseList(num2)
        
        carry = 0
        dummy_head = Node(0)  
        current = dummy_head
        
        while num1 or num2 or carry:
            sum_value = carry
            if num1:
                sum_value += num1.data
                num1 = num1.next
            if num2:
                sum_value += num2.data
                num2 = num2.next
            
            current.next = Node(sum_value % 10)
            carry = sum_value // 10
            current = current.next
        
        result = self.reverseList(dummy_head.next)
        
        while result and result.data == 0 and result.next:
            result = result.next
        
        return result
