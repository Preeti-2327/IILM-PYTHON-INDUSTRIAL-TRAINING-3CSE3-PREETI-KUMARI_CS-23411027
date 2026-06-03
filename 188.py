class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)

        if n < 2 or k == 0:
            return 0

        # If k is large, treat as unlimited transactions
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        buy = [float('-inf')] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            for i in range(1, k + 1):
                buy[i] = max(buy[i], sell[i - 1] - price)
                sell[i] = max(sell[i], buy[i] + price)

        return sell[k]
