class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        index = 0
        prefix = ''

        while len(strs[0]) > index:

            ref = strs[0][index]

            for word in strs[1:]:

                if len(word) > index:
                    if word[index] != ref:
                        return prefix
                else:
                    return prefix

            index += 1
            prefix = strs[0][:index]
        return prefix
