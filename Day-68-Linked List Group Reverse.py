"""Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""
class Solution:
    def reverseKGroup(self, head, k):
        if not head:
            return head

        curr = head
        prev = None
        next_node = curr.next
        count = 0

        while curr and count < k:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            count += 1

        if next_node:
            head.next = self.reverseKGroup(next_node, k)

        return prev
