class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        item_0 = strs[0]
        item_1 = strs[1]

        if len(item_0) < len(item_1):
            short = item_0
        else:
            short = item_1

        if item_0[:2] != item_1[:2]:
            return ""

        prefix = ""
        for j in range(2, len(short)):
            if item_0[:j] == item_1[:j]:
                prefix = item_0[:j]
                j += 1
            else:
                break

        for i in range(2, len(strs)):
            item = strs[i]

            x = item[:len(prefix)]

            while len(prefix) > 1:

                if item[:len(prefix)] == prefix:
                    return prefix
                else:
                    prefix = prefix[:len(prefix) - 1]

            else:
                return ''
        return prefix
