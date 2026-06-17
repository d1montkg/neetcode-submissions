class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lt = 0
        rt = len(nums) - 1
        count = len(nums)

        while lt <= rt:
            if nums[rt] == val:
                rt -= 1
                count -= 1
            else:
                if nums[lt] == val:
                    nums[lt], nums[rt] = nums[rt], nums[lt]
                    count -= 1
                    rt -= 1
                lt += 1
        
        return count
