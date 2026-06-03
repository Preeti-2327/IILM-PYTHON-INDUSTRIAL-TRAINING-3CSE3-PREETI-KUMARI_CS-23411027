class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(start, path, target):
            if len(path) == k:
                if target == 0:
                    res.append(path[:])
                return

            for num in range(start, 10):
                if num > target:
                    break

                path.append(num)
                backtrack(num + 1, path, target - num)
                path.pop()

        backtrack(1, [], n)
        return res
