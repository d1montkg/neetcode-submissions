class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums)):
            mult = 1
            for j in range(len(nums)):
                mult *= nums[j] if i != j else 1
            ans.append(mult)
        
        return ans
