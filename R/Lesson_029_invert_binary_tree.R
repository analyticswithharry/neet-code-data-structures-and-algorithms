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

invertTree <- function(node) {
    if (is.null(node)) return(NULL)
    list(val=node$val, left=invertTree(node$right), right=invertTree(node$left))
}
root <- list(val=4,
             left=list(val=2, left=list(val=1,left=NULL,right=NULL), right=list(val=3,left=NULL,right=NULL)),
             right=list(val=7, left=list(val=6,left=NULL,right=NULL), right=list(val=9,left=NULL,right=NULL)))
inv <- invertTree(root)
print(c(inv$val, inv$left$val, inv$right$val))
