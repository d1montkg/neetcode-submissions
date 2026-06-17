class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        word = strs[0]
        for i in range(len(strs)):
            while strs[i].find(word) != 0:
                word = word[0 : len(word) - 1]
                if word == "":
                    return ""
        return word