class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        counts = [0] * n
        arr = [(nums[i], i) for i in range(n)]

        def merge_sort(left, right):
            if right - left <= 1:
                return

            mid = (left + right) // 2
            merge_sort(left, mid)
            merge_sort(mid, right)

            temp = []
            i, j = left, mid
            right_count = 0

            while i < mid and j < right:
                if arr[j][0] < arr[i][0]:
                    temp.append(arr[j])
                    right_count += 1
                    j += 1
                else:
                    counts[arr[i][1]] += right_count
                    temp.append(arr[i])
                    i += 1

            while i < mid:
                counts[arr[i][1]] += right_count
                temp.append(arr[i])
                i += 1

            while j < right:
                temp.append(arr[j])
                j += 1

            arr[left:right] = temp

        merge_sort(0, n)
        return counts
