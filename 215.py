class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k = len(nums) - k  # kth largest -> kth smallest index

        def quickSelect(left, right):
            pivot = nums[right]
            p = left

            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            nums[p], nums[right] = nums[right], nums[p]

            if p == k:
                return nums[p]
            elif p < k:
                return quickSelect(p + 1, right)
            else:
                return quickSelect(left, p - 1)

        return quickSelect(0, len(nums) - 1)
