// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 014 -- Lowest Common Ancestor of a Binary Search Tree
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 7
// =============================================================
//
// QUESTION:
//   Given a binary search tree (BST), find the lowest common ancestor (LCA)
//   of two given nodes p and q. Both p and q exist in the BST.
//
//   Example:
//     Input : root=[6,2,8,0,4,7,9,null,null,3,5], p=2, q=8
//     Output: 6
// =============================================================

function TreeNode(v,l,r){this.val=v??0;this.left=l??null;this.right=r??null;}
var lowestCommonAncestor = function(root, p, q) {
    let cur = root;
    while (cur) {
        if (p.val < cur.val && q.val < cur.val) cur = cur.left;
        else if (p.val > cur.val && q.val > cur.val) cur = cur.right;
        else return cur;
    }
};
const n2 = new TreeNode(2), n8 = new TreeNode(8);
const root = new TreeNode(6, n2, n8);
console.log(lowestCommonAncestor(root, n2, n8).val); // 6
