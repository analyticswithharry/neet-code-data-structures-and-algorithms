// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 179 -- Construct Binary Tree From Preorder And Inorder Traversal
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 90
// =============================================================
//
// QUESTION:
//   Given preorder and inorder traversals (no duplicates), reconstruct the binary tree.
// =============================================================
class N{constructor(v,l=null,r=null){this.v=v;this.l=l;this.r=r;}}
function build(pre,ino){const idx=new Map();ino.forEach((v,i)=>idx.set(v,i));let p=0;function rec(lo,hi){if(lo>hi)return null;const v=pre[p++];const k=idx.get(v);const n=new N(v);n.l=rec(lo,k-1);n.r=rec(k+1,hi);return n;}return rec(0,ino.length-1);}
function pre_order(n){if(!n)return [];return [n.v,...pre_order(n.l),...pre_order(n.r)];}
console.log(pre_order(build([3,9,20,15,7],[9,3,15,20,7])));
