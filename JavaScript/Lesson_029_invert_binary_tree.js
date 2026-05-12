// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 029 -- Invert Binary Tree
// Category   : Trees
// Difficulty : Easy
// Study Plan : Day 15
// =============================================================
//
// QUESTION:
//   Given the root of a binary tree, invert the tree (mirror it), and
//   return its root.
//
//   Example:
//     Input : [4,2,7,1,3,6,9]
//     Output: [4,7,2,9,6,3,1]
// =============================================================

function TreeNode(v,l,r){this.val=v??0;this.left=l??null;this.right=r??null;}
var invertTree = function(root) {
    if (!root) return null;
    [root.left, root.right] = [invertTree(root.right), invertTree(root.left)];
    return root;
};
const r = new TreeNode(4, new TreeNode(2, new TreeNode(1), new TreeNode(3)), new TreeNode(7, new TreeNode(6), new TreeNode(9)));
const inv = invertTree(r);
console.log(inv.val, inv.left.val, inv.right.val);
