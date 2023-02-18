from leetcode.add_two_numbers.solution import add_two_numbers, ListNode


def test_add_two_numbers():
    l13 = ListNode(val=3)
    l12 = ListNode(val=4, next=l13)
    l11 = ListNode(val=2, next=l12)

    l23 = ListNode(val=4)
    l22 = ListNode(val=6, next=l23)
    l21 = ListNode(val=5, next=l22)

    lo3 = ListNode(val=8)
    lo2 = ListNode(val=0, next=lo3)
    lo1 = ListNode(val=7, next=lo2)

    assert add_two_numbers(l1=l11, l2=l21) == lo1
    assert add_two_numbers(l1=l11, l2=l21).next == lo1.next
    assert add_two_numbers(l1=l11, l2=l21).next.next == lo1.next.next
    assert add_two_numbers(l1=l11, l2=l21).next.next.next == lo1.next.next.next
