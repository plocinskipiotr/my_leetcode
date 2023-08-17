import pytest
from problems.easy.add_binary.src.add_binary import Solution
from problems.easy.add_binary.test.test_input import load_test_input


class TestSolution:

    @pytest.mark.parametrize('test_input,expected', load_test_input())
    def test_add_binary(self, test_input, expected):
        assert Solution().addBinary(*test_input) == expected
