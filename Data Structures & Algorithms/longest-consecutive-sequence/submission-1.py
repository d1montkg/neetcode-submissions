class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        seen = set()
        uniq_nums = set(nums)
        max_count = 1

        for num in nums:
            if num in seen:
                continue
            seen.add(num)

            value = num + 1
            if value in uniq_nums:
                count = 1
                while value in uniq_nums:
                    count += 1
                    seen.add(value)
                    value += 1
                max_count = max(count, max_count)
        
        return max_count