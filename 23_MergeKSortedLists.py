# 23. Merge k Sorted Lists

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    heap = []
    
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    
    dummy = ListNode(0)
    current = dummy
    
    while heap:
        val, i, node = heapq.heappop(heap)
        
        current.next = node
        current = current.next
        
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next


def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


if __name__ == "__main__":
    # List 1: 1 -> 4 -> 5
    l1 = ListNode(1, ListNode(4, ListNode(5)))

    # List 2: 1 -> 3 -> 4
    l2 = ListNode(1, ListNode(3, ListNode(4)))

    # List 3: 2 -> 6
    l3 = ListNode(2, ListNode(6))

    lists = [l1, l2, l3]

    result = mergeKLists(lists)

    print("Merged List:")
    printList(result)