// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 030 -- Maximum Depth of Binary Tree
// Category   : Trees
// Difficulty : Easy
// Study Plan : Day 15
// =============================================================
//
// QUESTION:
//   Given the root of a binary tree, return its maximum depth (number of
//   nodes along the longest path from the root down to the farthest leaf).
//
//   Example:
//     Input : [3,9,20,null,null,15,7]
//     Output: 3
// =============================================================

function TreeNode(v,l,r){this.val=v??0;this.left=l??null;this.right=r??null;}
var maxDepth = function(root) {
    if (!root) return 0;
    return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
};
console.log(maxDepth(new TreeNode(3, new TreeNode(9), new TreeNode(20, new TreeNode(15), new TreeNode(7)))));
