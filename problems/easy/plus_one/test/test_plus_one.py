import pytest
from problems.easy.plus_one.src.plus_one import Solution
from problems.easy.plus_one.test.test_input import load_test_input


class TestSolution:

    @pytest.mark.parametrize('test_input,expected', load_test_input())
    def test_plus_one_0(self, test_input, expected):
        assert Solution().plusOne(test_input) == expected
