from typing import Optional

from itertools import zip_longest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        return self.val == other.val and self.next == other.next


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    l1l = []
    while True:
        l1l.append(l1.val)
        if l1.next is None:
            break
        else:
            l1 = l1.next

    l2l = []
    while True:
        l2l.append(l2.val)
        if l2.next is None:
            break
        else:
            l2 = l2.next

    lol = []
    lo_rest = 0
    for i, j in zip_longest(l1l, l2l, fillvalue=0):
        lo_val = i + j + lo_rest
        if lo_val >= 10:
            lo_val = lo_val - 10
            lo_rest = 1
        else:
            lo_rest = 0
        lol.append(lo_val)

    if lo_rest == 1:
        lol.append(1)

    lo_item = None
    for i, val in enumerate(lol[::-1]):
        lo_next = lo_item
        lo_item = ListNode(val=val, next=lo_next)

    return lo_item
