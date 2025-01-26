class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        slow, fast = head, head
        while fast and fast.next and (slow := slow.next) != (fast := fast.next.next): pass
        if not fast or not fast.next: return
        slow = head
        while slow != fast: slow, fast = slow.next, fast.next
        while fast.next != slow: fast = fast.next
        fast.next = None
