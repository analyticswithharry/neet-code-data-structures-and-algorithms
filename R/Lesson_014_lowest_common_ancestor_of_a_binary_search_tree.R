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

lowestCommonAncestor <- function(root, p, q) {
    cur <- root
    while (!is.null(cur)) {
        if (p < cur$val && q < cur$val) cur <- cur$left
        else if (p > cur$val && q > cur$val) cur <- cur$right
        else return(cur$val)
    }
    NA
}
root <- list(val=6,
             left=list(val=2, left=NULL, right=NULL),
             right=list(val=8, left=NULL, right=NULL))
print(lowestCommonAncestor(root, 2, 8))  # 6
