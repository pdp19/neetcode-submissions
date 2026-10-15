class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merged = sorted(nums1 + nums2)
        # n = len(merged)
        # if n % 2 == 1:
        #     return float(merged[n//2])
        # return (merged[n//2-1] + merged[n//2])/2.0
        #Solution - 2
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        l, r = 0, m

        while l <= r:
            i = (l+r)//2
            j = (m+n+1)//2 - i

            l1 = float('-inf') if i == 0 else nums1[i-1]
            r1 = float('inf') if i == m else nums1[i]

            l2 = float('-inf') if j == 0 else nums2[j-1]
            r2 = float('inf') if j == n else nums2[j]

            if l1 <= r2 and l2 <= r1:
                if (m+n)%2:
                    return float(max(l1, l2))
                return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                r = i - 1
            else:
                l = i + 1
        return 0.0


        