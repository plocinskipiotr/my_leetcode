import pytest
from problems.easy.roman_integer.src.roman_integer import Solution
from problems.easy.roman_integer.test.test_input import load_test_input


class TestSolution:
    @pytest.mark.parametrize("test_input,expected", load_test_input())
    def test_roman_to_int(self, test_input, expected):
        assert Solution().romanToInt(test_input) == expected
