
class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True
        return False
