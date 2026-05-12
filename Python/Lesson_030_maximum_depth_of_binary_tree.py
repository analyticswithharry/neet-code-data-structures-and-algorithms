# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 030 -- Maximum Depth of Binary Tree
# Category   : Trees
# Difficulty : Easy
# Study Plan : Day 15
# =============================================================
#
# QUESTION:
#   Given the root of a binary tree, return its maximum depth (number of
#   nodes along the longest path from the root down to the farthest leaf).
#
#   Example:
#     Input : [3,9,20,null,null,15,7]
#     Output: 3
# =============================================================

class TreeNode:
    def __init__(self, v=0, l=None, r=None): self.val, self.left, self.right = v, l, r
class Solution:
    def maxDepth(self, root):
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(Solution().maxDepth(root))  # 3
