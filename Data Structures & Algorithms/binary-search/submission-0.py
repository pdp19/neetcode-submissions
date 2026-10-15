class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1
        m = (l + r)//2

        # for i, num in enumerate(nums):
        while l <= r:
            if nums[m] == target:
                return m
            elif target > nums[m]:
                l = m + 1
                m = (l+r)//2
            else:
                r = m -1
                m = (l+r)//2
        return -1

        