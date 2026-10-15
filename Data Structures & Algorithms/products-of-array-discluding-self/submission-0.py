class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # res = []
        # for i in range(n):
        #     temp = 1
        #     for j in range(n):
        #         if i != j:
        #             temp *= nums[j]
        #     res.append(temp)
        # return res
        res = [1] * n
        prefix = 1
        for i in range(n):
            res[i] = prefix 
            prefix *= nums[i]
        suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res


        