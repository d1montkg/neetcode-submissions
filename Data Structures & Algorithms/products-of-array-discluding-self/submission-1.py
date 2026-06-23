class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult = 1
        count_zero = 0

        for num in nums:
            if num == 0:
                count_zero += 1
            else:
                mult *= num
    
        if count_zero > 1:
            return [0] * len(nums)
        
        ans = [0] * len(nums)
        for i, num in enumerate(nums):
            if count_zero:
                ans[i] = 0 if num else mult
            else:
                ans[i] = mult // num

        return ans
