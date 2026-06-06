class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + [x for x in nums if x > 0] + [1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        for length in range(1, n - 1):
            for left in range(1, n - length):
                right = left + length - 1

                for k in range(left, right + 1):
                    dp[left][right] = max(
                        dp[left][right],
                        dp[left][k - 1]
                        + nums[left - 1] * nums[k] * nums[right + 1]
                        + dp[k + 1][right]
                    )

        return dp[1][n - 2]
