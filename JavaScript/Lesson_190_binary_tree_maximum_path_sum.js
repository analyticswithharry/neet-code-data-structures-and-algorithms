// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 190 -- Binary Tree Maximum Path Sum
// Category   : Trees
// Difficulty : Hard
// Study Plan : Day 95
// =============================================================
//
// QUESTION:
//   Path is any sequence of nodes connected by edges (with at least one node). Return the maximum sum.
// =============================================================
class N{constructor(v,l=null,r=null){this.v=v;this.l=l;this.r=r;}}
function maxPathSum(root){let res=-Infinity;function dfs(n){if(!n)return 0;const l=Math.max(0,dfs(n.l)),r=Math.max(0,dfs(n.r));res=Math.max(res,n.v+l+r);return n.v+Math.max(l,r);}dfs(root);return res;}
console.log(maxPathSum(new N(1,new N(2),new N(3))));console.log(maxPathSum(new N(-10,new N(9),new N(20,new N(15),new N(7)))));
