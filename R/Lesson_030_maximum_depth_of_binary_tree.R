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

maxDepth <- function(node) {
    if (is.null(node)) return(0)
    1 + max(maxDepth(node$left), maxDepth(node$right))
}
root <- list(val=3,
             left=list(val=9, left=NULL, right=NULL),
             right=list(val=20, left=list(val=15,left=NULL,right=NULL), right=list(val=7,left=NULL,right=NULL)))
print(maxDepth(root))
