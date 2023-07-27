import pytest
from problems.easy.remove_duplicates_from_sorted_array.src.remove_duplicates_from_sorted_array import Solution
from problems.easy.remove_duplicates_from_sorted_array.tests.test_input import load_test_input


class TestSolution:

    @pytest.mark.parametrize('test_input,expected', load_test_input())
    def test_remove_duplicates_0(self, test_input, expected):
        x = Solution().removeDuplicates(test_input)
        assert x == expected
