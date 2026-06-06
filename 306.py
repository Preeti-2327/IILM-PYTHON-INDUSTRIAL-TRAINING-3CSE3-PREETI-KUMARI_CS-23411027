class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)

        def valid(a, b, start):
            while start < n:
                c = str(int(a) + int(b))

                if not num.startswith(c, start):
                    return False

                start += len(c)
                a, b = b, c

            return True

        for i in range(1, n):
            for j in range(i + 1, n):

                a = num[:i]
                b = num[i:j]

                if (len(a) > 1 and a[0] == '0') or \
                   (len(b) > 1 and b[0] == '0'):
                    continue

                if valid(a, b, j):
                    return True

        return False
