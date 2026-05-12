# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 029 -- Invert Binary Tree
# Category   : Trees
# Difficulty : Easy
# Study Plan : Day 15
# =============================================================
#
# QUESTION:
#   Given the root of a binary tree, invert the tree (mirror it), and
#   return its root.
#
#   Example:
#     Input : [4,2,7,1,3,6,9]
#     Output: [4,7,2,9,6,3,1]
# =============================================================

class TreeNode:
    def __init__(self, v=0, l=None, r=None): self.val, self.left, self.right = v, l, r

class Solution:
    def invertTree(self, root):
        if not root: return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

def lvl(r):
    out, q = [], [r]
    while q:
        n = q.pop(0)
        if n: out.append(n.val); q.append(n.left); q.append(n.right)
        else: out.append(None)
    while out and out[-1] is None: out.pop()
    return out

if __name__ == "__main__":
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    print(lvl(Solution().invertTree(root)))
