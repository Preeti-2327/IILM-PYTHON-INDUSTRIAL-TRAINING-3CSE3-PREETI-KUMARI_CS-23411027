class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        self.nums = nums[:]
        self.bit = [0] * (self.n + 1)

        for i in range(self.n):
            self._updateBIT(i + 1, nums[i])

    def _updateBIT(self, index, delta):
        while index <= self.n:
            self.bit[index] += delta
            index += index & -index

    def _query(self, index):
        s = 0
        while index > 0:
            s += self.bit[index]
            index -= index & -index
        return s

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        delta = val - self.nums[index]
        self.nums[index] = val
        self._updateBIT(index + 1, delta)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self._query(right + 1) - self._query(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index, val)
# param_2 = obj.sumRange(left, right)
