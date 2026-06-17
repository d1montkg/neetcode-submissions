class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        uniq_nums = {}

        for i in range(len(nums)):
            uniq_nums[nums[i]] = uniq_nums.get(nums[i], 0) + 1
        
        return max(uniq_nums, key=uniq_nums.get)
