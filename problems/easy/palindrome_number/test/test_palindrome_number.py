import pytest
from problems.easy.palindrome_number.src.palindrome_number import Solution
from problems.easy.palindrome_number.test.test_input import load_test_input


class TestSolution:

    @pytest.mark.parametrize("test_input,expected", load_test_input())
    def tests(self, test_input, expected):
        assert Solution().isPalindrome(test_input) == expected
