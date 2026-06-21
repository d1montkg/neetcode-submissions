class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ans = []
        
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        
        sorted_count = dict(sorted(count.items(), key=lambda item: item[1]))
        sorted_keys = list(sorted_count.keys())

        for i in range(k):
            ans.append(sorted_keys[len(sorted_keys) - i - 1])
        
        return ans
