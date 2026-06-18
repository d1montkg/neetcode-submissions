class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = nums[len(nums) // 2]
        less = list(filter(lambda x: x < mid, nums))
        centre = [x for x in nums if x == mid]
        more = list(filter(lambda x: x > mid, nums))

        return self.sortArray(less) + centre + self.sortArray(more)