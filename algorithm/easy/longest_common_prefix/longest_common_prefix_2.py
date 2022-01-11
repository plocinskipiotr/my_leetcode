class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        try:
            prefix = strs[1]
        except IndexError:
            return strs[0]

        for j in range(len(strs)):
            item_0 = strs[j]
            new_prefix = ''
            for i in range(len(item_0)):
                try:
                    if item_0[:i + 1] == prefix[:i + 1]:
                        new_prefix = prefix[:i + 1]
                    else:
                        if new_prefix == '':
                            return ''
                        break
                except IndexError:
                    break
            prefix = new_prefix

        if len(prefix) < 1:
            return ''

        return prefix
