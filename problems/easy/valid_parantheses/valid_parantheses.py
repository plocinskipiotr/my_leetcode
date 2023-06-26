class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = {'{', '[', '('}
        closed_brackets = {'}', ']', ')'}
        brackets = {'}': '{',
                    ']': '[',
                    ')': '('}

        stack = list()
        for char in s:

            if char in open_brackets:
                stack.append(char)

            if char in closed_brackets:
                if len(stack) == 0:
                    return False
                el = stack.pop()
                if el != brackets[char]:
                    return False

        if len(stack) > 0:
            return False

        return True
