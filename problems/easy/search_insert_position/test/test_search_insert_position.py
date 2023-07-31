import pytest
from problems.easy.search_insert_position.src.search_insert_position import Solution
from problems.easy.search_insert_position.test.test_input import load_test_input


class TestSolution:
    @pytest.mark.parametrize("test_input,expected", load_test_input())
    def test_search_insert_0(self, test_input, expected):
        nums, target = test_input
        assert Solution().searchInsert(nums, target) == expected
