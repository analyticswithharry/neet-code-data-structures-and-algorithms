// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 180 -- House Robber III
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 90
// =============================================================
//
// QUESTION:
//   Houses arranged as a binary tree; cannot rob two directly-linked houses. Return max amount.
// =============================================================
class N{constructor(v,l=null,r=null){this.v=v;this.l=l;this.r=r;}}
function rob(root){function rec(n){if(!n)return [0,0];const l=rec(n.l),r=rec(n.r);return [n.v+l[1]+r[1], Math.max(l[0],l[1])+Math.max(r[0],r[1])];}return Math.max(...rec(root));}
console.log(rob(new N(3,new N(2,null,new N(3)),new N(3,null,new N(1)))));
