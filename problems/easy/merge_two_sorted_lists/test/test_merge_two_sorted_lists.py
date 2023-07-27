import pytest

from problems.easy.merge_two_sorted_lists.src.merge_two_sorted_lists import Solution
from problems.easy.merge_two_sorted_lists.test.test_input import load_test_input


class TestSolution:
    @pytest.mark.parametrize("test_input,expected", load_test_input())
    def test_merge_two_lists_0(self, test_input, expected):
        a, b = test_input
        x = Solution().mergeTwoLists(a, b)
        assert x.to_int_list() == expected.to_int_list()
