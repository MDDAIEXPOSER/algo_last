class Solution(object):
    def tribonacci(self, n):
        treenode_root = 0
        treenode_1 = 1
        treenode_2 = 1

        if n == 0:
            return treenode_root

        if n == 1 or n == 2:
            return treenode_1

        for i in range(3, n+1):
            treenodev = treenode_root + treenode_1 + treenode_2
            treenode_root = treenode_1
            treenode_1 = treenode_2
            treenode_2 = treenodev

        return treenodev p
