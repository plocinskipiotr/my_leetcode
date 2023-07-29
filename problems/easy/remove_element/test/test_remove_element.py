import pytest
from problems.easy.remove_element.src.remove_element import Solution
from problems.easy.remove_element.test.test_input import load_test_input


class TestSolution:
    @pytest.mark.parametrize('test_input,expected', load_test_input())
    def test_remove_element(self, test_input, expected):
        val = 2
        data = [1, 2, 2, 3, 4, 5]

        x = Solution().removeElement(data, val)

        nums, val = test_input

        assert Solution().removeElement(nums, val) == expected
