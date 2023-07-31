import pytest
from problems.easy.length_of_last_word.src.length_of_last_word import Solution
from problems.easy.length_of_last_word.test.test_input import load_test_input


class TestSolution:
    @pytest.mark.parametrize("test_input,expected", load_test_input())
    def test_length_of_last_word(self, test_input, expected):
        assert Solution().lengthOfLastWord(test_input) == expected
