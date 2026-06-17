class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        flag = 0
        min_word = min([len(word) for word in strs])

        for i in range(min_word):
            if flag == 1:
                break
            symb = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != symb:
                    flag = 1
                    break
            else:
                ans += symb

        return ans
        