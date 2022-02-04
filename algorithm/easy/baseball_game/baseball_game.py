from typing import List


class Solution:

    def new_sum_score(self, stack: list):
        stack.append(stack[-2] + stack[-1])
        return stack

    def new_double_score(self, stack: list):
        stack.append(stack[-1] * 2)
        return stack

    def remove_score(self, stack: list):
        stack.pop()
        return stack

    def new_score(self, value, stack: list):
        stack.append(value)
        return stack

    def translate(self, char, stack):
        if char == '+':
            return self.new_sum_score(stack)
        elif char == 'D':
            return self.new_double_score(stack)
        elif char == 'C':
            return self.remove_score(stack)
        else:
            return self.new_score(int(char), stack)

    def calPoints(self, ops: List[str]) -> int:
        suma = 0
        lst = list()
        for op in ops:
            lst = self.translate(op, lst)
        return sum(lst)
