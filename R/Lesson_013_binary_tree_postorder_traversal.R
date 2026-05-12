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

postorderTraversal <- function(node) {
    if (is.null(node)) return(integer(0))
    c(postorderTraversal(node$left), postorderTraversal(node$right), node$val)
}
root <- list(val=1, left=NULL, right=list(val=2, left=list(val=3, left=NULL, right=NULL), right=NULL))
print(postorderTraversal(root))  # 3 2 1
