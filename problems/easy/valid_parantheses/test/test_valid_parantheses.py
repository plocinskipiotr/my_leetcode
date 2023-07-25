import pytest

from problems.easy.valid_parantheses.src.valid_parantheses import Solution
from problems.easy.valid_parantheses.test.test_input import load_test_input


class TestSolution:

    @pytest.mark.parametrize("test_input,expected", load_test_input())
    def test_is_valid(self, test_input, expected):
        assert Solution().isValid(test_input) == expected
