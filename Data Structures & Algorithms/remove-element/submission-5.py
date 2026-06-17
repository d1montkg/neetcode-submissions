class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        total_values = len(nums)

        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = '_'
                total_values -= 1

        lt, rt = 0, len(nums) - 1
        while lt < rt:
            if nums[rt] == '_':
                rt -= 1
            else:
                if nums[lt] == '_':
                    nums[lt], nums[rt] = nums[rt], nums[lt]
                lt += 1
            
        
        return total_values
