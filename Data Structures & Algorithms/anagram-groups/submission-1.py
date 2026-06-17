class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        input_nums = []

        for i in range(len(strs)):
            if strs[i] not in input_nums:
                inter_ans = [strs[i]]
                input_nums.append(strs[i])
            
                for j in range(len(strs)):
                    if i != j:
                        count = {}
                        for char in strs[i]:
                            count[char] = count.get(char, 0) + 1
                        for char in strs[j]:
                            count[char] = count.get(char, 0) - 1

                        if all(value == 0 for value in count.values()):
                            inter_ans.append(strs[j])
                            input_nums.append(strs[j])
                ans.append(inter_ans)
        
        return ans
