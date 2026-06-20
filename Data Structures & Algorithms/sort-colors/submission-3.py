class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero = one = 0
        for two in range(len(nums)):
            cur_elem = nums[two]
            nums[two] = 2
            if cur_elem < 2:
                nums[one] = 1
                one += 1
            if cur_elem < 1:
                nums[zero] = 0
                zero += 1
        