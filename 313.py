class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        k = len(primes)

        ugly = [1] * n
        idx = [0] * k
        vals = primes[:]

        for i in range(1, n):
            nxt = min(vals)
            ugly[i] = nxt

            for j in range(k):
                if vals[j] == nxt:
                    idx[j] += 1
                    vals[j] = primes[j] * ugly[idx[j]]

        return ugly[-1]
