from collections import Counter

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        s_count = Counter()
        g_count = Counter()

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                s_count[s] += 1
                g_count[g] += 1

        cows = 0
        for digit in s_count:
            cows += min(s_count[digit], g_count[digit])

        return str(bulls) + "A" + str(cows) + "B"
