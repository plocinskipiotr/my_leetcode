from typing import Literal

bracket = Literal['[', ']', '(', ')', '{', '}']


def pair_up(el_1: bracket, el_2: bracket):
    match el_1 + el_2:
        case '{}':
            return True
        case '()':
            return True
        case '[]':
            return True
        case _:
            return False


class Solution:
    def isValid(self, s: list[Literal]) -> bool:

        stack: list[Literal] = []
        for el in s:

            if el in '{([':
                stack.append(el)
            elif len(stack) > 0 and pair_up(stack[-1], el):
                    stack.pop()
            else:
                return False

        return len(stack) == 0
