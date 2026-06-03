# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def getHeight(self, node):
        h = 0
        while node:
            h += 1
            node = node.left
        return h

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)

        if left_height == right_height:
            # perfect tree
            return (1 << left_height) + self.countNodes(root.right)
        else:
            # left subtree is perfect of height right_height
            return (1 << right_height) + self.countNodes(root.left)
