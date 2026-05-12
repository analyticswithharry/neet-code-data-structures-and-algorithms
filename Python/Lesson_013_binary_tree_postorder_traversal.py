# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 013 -- Binary Tree Postorder Traversal
# Category   : Trees
# Difficulty : Easy
# Study Plan : Day 7
# =============================================================
#
# QUESTION:
#   Given the root of a binary tree, return the postorder
#   (Left, Right, Root) traversal of its nodes' values.
#
#   Example:
#     Input : root = [1,null,2,3]
#     Output: [3, 2, 1]
# =============================================================

class TreeNode:
    def __init__(self, v=0, l=None, r=None): self.val, self.left, self.right = v, l, r

class Solution:
    def postorderTraversal(self, root):
        out, st = [], []
        cur, last = root, None
        while cur or st:
            while cur: st.append(cur); cur = cur.left
            peek = st[-1]
            if peek.right and last is not peek.right:
                cur = peek.right
            else:
                out.append(peek.val); last = st.pop()
        return out

if __name__ == "__main__":
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    print(Solution().postorderTraversal(root))  # [3,2,1]
