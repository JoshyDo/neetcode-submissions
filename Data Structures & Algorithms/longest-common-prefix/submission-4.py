class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for i, c in enumerate(strs[0]):
            for s in strs[1::]:
                if i < len(s) and c == s[i]:
                    continue
                else:
                    return res
            res += c
        return res