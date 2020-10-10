from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()


def reorder(head):
    slow, fast = head, head

    pre = None
    while fast and fast.next:
        pre = slow
        slow = slow.next
        fast = fast.next.next
    pre.next = None
    pre = None
    while slow:
        next = slow.next
        slow.next = pre
        pre = slow
        slow = next

    cur = head

    while cur:
        next = cur.next
        cur.next = pre
        cur = next

        next = pre.next
        pre.next = cur
        pre = next
    return head

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    reorder(head)
    head.print_list()


main()
