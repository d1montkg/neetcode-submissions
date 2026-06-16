class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        available_nums = {}

        for i in range(len(nums)):
            x = target - nums[i]
            if x in available_nums:
                return [available_nums[x], i]
            available_nums[nums[i]] = i
        
        return []