class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        available_nums = {}

        for i, num in enumerate(nums):
            x = target - num
            if x in available_nums:
                return [available_nums[x], i]
            available_nums[num] = i
        
        return []