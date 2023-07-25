import pytest

from problems.easy.longest_common_prefix.src.longest_common_prefix import Solution
from problems.easy.longest_common_prefix.test.test_input import load_test_input


class TestSolution:
    @pytest.mark.parametrize("test_input,expected", load_test_input())
    def test_longest_common_prefix(self, test_input, expected):
        assert Solution().longestCommonPrefix(test_input) == expected
