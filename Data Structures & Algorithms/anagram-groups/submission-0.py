class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        input_nums = []

        for i in range(len(strs)):
            if strs[i] not in input_nums:
                general_word = sorted(strs[i])
                inter_ans = [strs[i]]
                input_nums.append(strs[i])

                for j in range(len(strs)):
                    add_word = sorted(strs[j])
                    if general_word == add_word and i != j:
                        inter_ans.append(strs[j])
                        input_nums.append(strs[j])
                
                ans.append(inter_ans)

        return ans
