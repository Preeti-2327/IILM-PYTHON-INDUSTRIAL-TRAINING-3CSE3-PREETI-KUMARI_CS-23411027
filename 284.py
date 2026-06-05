# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.next_element = iterator.next() if iterator.hasNext() else None

    def peek(self):
        """
        :rtype: int
        """
        return self.next_element

    def next(self):
        """
        :rtype: int
        """
        current = self.next_element

        if self.iterator.hasNext():
            self.next_element = self.iterator.next()
        else:
            self.next_element = None

        return current

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.next_element is not None
