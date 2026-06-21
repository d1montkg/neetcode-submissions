class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def heapify(nums, i, n):
            general = i
            left = i * 2 + 1
            right = i * 2 + 2

            if left < n and nums[left] > nums[general]:
                general = left
            
            if right < n and nums[right] > nums[general]:
                general = right
            
            if general != i:
                nums[i], nums[general] = nums[general], nums[i]
                heapify(nums, general, n)
        
        def heapSort(nums):
            n = len(nums)

            for i in range(n // 2 - 1, -1, -1):
                heapify(nums, i, n)
        
            for i in range(n - 1, 0, -1):
                nums[0], nums[i] = nums[i], nums[0]
                heapify(nums, 0, i)

        heapSort(nums)
        return nums
