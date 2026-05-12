// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 013 -- Binary Tree Postorder Traversal
// Category   : Trees
// Difficulty : Easy
// Study Plan : Day 7
// =============================================================
//
// QUESTION:
//   Given the root of a binary tree, return the postorder
//   (Left, Right, Root) traversal of its nodes' values.
//
//   Example:
//     Input : root = [1,null,2,3]
//     Output: [3, 2, 1]
// =============================================================

function TreeNode(v,l,r){this.val=v??0;this.left=l??null;this.right=r??null;}
var postorderTraversal = function(root) {
    const out = [], st = [];
    let cur = root, last = null;
    while (cur || st.length) {
        while (cur) { st.push(cur); cur = cur.left; }
        const peek = st[st.length-1];
        if (peek.right && last !== peek.right) cur = peek.right;
        else { out.push(peek.val); last = st.pop(); }
    }
    return out;
};
console.log(postorderTraversal(new TreeNode(1,null,new TreeNode(2,new TreeNode(3)))));
