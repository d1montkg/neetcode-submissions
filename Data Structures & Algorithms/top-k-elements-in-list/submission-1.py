class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        ans = []

        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1

        for i in range(k):
            mx = -1001
            for key, val in count.items():
                if val > mx:
                    mx = val
                    appropriate_value = key

            ans.append(appropriate_value)
            count[appropriate_value] = -1001

        return ans
