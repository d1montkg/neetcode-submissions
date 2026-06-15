class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return not (sorted(set(nums)) == sorted(nums))