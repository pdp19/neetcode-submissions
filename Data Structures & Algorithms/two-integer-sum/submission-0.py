class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0 
        r = n = len(nums)
        # for i in range(0, n):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return None
        seen = {}
        for i in range(0, n):
            remainder = target - nums[i]
            if remainder in seen:
                return [seen[remainder], i]
            seen[nums[i]] = i
