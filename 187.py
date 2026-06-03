class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen = set()
        repeated = set()

        for i in range(len(s) - 9):
            seq = s[i:i + 10]

            if seq in seen:
                repeated.add(seq)
            else:
                seen.add(seq)

        return list(repeated)
