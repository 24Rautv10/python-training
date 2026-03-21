class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        
        return None


# --------- Testing in VS Code ---------

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

# create nodes
a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(-4)

# link nodes
a.next = b
b.next = c
c.next = d
d.next = b  # cycle

# create object AFTER class definition
obj = Solution()

result = obj.detectCycle(a)

if result:
    print(result.val)
else:
    print("No cycle")