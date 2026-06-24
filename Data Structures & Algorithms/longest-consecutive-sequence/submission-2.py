class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq_nums = set(nums)
        longest = 0

        for num in uniq_nums:
            if (num - 1) not in uniq_nums:
                length = 1
                while (num + length) in uniq_nums:
                    length += 1
                longest = max(length, longest)
        
        return longest