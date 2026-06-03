class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        stack = []
        num = 0
        sign = '+'
        s = s.strip()

        for i in range(len(s)):
            ch = s[i]

            if ch.isdigit():
                num = num * 10 + int(ch)

            if ch in "+-*/" or i == len(s) - 1:

                if sign == '+':
                    stack.append(num)

                elif sign == '-':
                    stack.append(-num)

                elif sign == '*':
                    stack.append(stack.pop() * num)

                elif sign == '/':
                    top = stack.pop()
                    # truncate toward zero
                    stack.append(int(top / num))

                sign = ch
                num = 0

        return sum(stack)
