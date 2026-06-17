class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for i in range(len(strs)):
            word_sorted = ''.join(sorted(strs[i]))
            ans[word_sorted].append(strs[i])
        
        return list(ans.values())
