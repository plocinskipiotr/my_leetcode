from problems.easy.merge_two_sorted_lists.src.merge_two_sorted_lists import ListNode

TEST_INPUT = \
    [
        ([ListNode.from_list([2, 2]),
          ListNode.from_list([1])], ListNode.from_list([1, 2, 2])),

        ([ListNode.from_list([1, 1]),
          ListNode.from_list([2])], ListNode.from_list([1, 1, 2])),

        ([ListNode.from_list([1, 1, 1, 1, 1]),
          ListNode.from_list([5, 5, 5, 5, 5])], ListNode.from_list([1, 1, 1, 1, 1, 5, 5, 5, 5, 5])),

        ([ListNode.from_list([1, 2, 4]),
          ListNode.from_list([1, 3, 4])], ListNode.from_list([1, 1, 2, 3, 4, 4])),

        ([ListNode.from_list([5, 5, 5, 5]),
          ListNode.from_list([1, 1, 1, 1])], ListNode.from_list([1, 1, 1, 1, 5, 5, 5, 5])),

        ([ListNode.from_list([0]),
          ListNode.from_list([0])], ListNode.from_list([0, 0])),

        ([ListNode.from_list([]),
          ListNode.from_list([5])], ListNode.from_list([5])),

        ([ListNode.from_list([]),
          ListNode.from_list([])], ListNode.from_list([])),

        ([ListNode.from_list([5]),
          ListNode.from_list([])], ListNode.from_list([5]))

    ]


#


def load_test_input():
    return TEST_INPUT
