class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        factor = 1
        count = 0

        while factor <= n:
            lower = n % factor
            current = (n // factor) % 10
            higher = n // (factor * 10)

            if current == 0:
                count += higher * factor
            elif current == 1:
                count += higher * factor + lower + 1
            else:
                count += (higher + 1) * factor

            factor *= 10

        return count
