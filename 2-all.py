# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        stacking = []

        prevert = float('inf')
        medium = float('inf')

        current = root

        while stacking or current:
            if current:
               stacking.append(current)
               current = current.left
            else:
                current = stacking.pop()

                if prevert == float('inf'):
                    prevert = current.val
                else:
                    medium = min(medium, abs(prevert - current.val))
                    prevert = current.val
                current = current.right
        return medium
