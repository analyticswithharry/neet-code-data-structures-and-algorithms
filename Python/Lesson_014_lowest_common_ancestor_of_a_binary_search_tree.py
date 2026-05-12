# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 014 -- Lowest Common Ancestor of a Binary Search Tree
# Category   : Trees
# Difficulty : Medium
# Study Plan : Day 7
# =============================================================
#
# QUESTION:
#   Given a binary search tree (BST), find the lowest common ancestor (LCA)
#   of two given nodes p and q. Both p and q exist in the BST.
#
#   Example:
#     Input : root=[6,2,8,0,4,7,9,null,null,3,5], p=2, q=8
#     Output: 6
# =============================================================

class TreeNode:
    def __init__(self, v=0, l=None, r=None): self.val, self.left, self.right = v, l, r

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        cur = root
        while cur:
            if p.val < cur.val and q.val < cur.val: cur = cur.left
            elif p.val > cur.val and q.val > cur.val: cur = cur.right
            else: return cur

if __name__ == "__main__":
    n0,n3,n4,n5,n7,n9 = TreeNode(0),TreeNode(3),TreeNode(4),TreeNode(5),TreeNode(7),TreeNode(9)
    n4.left,n4.right = n3,n5
    n2 = TreeNode(2,n0,n4); n8 = TreeNode(8,n7,n9)
    root = TreeNode(6,n2,n8)
    print(Solution().lowestCommonAncestor(root, n2, n8).val)  # 6
