// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 175 -- Validate Binary Search Tree
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 88
// =============================================================
//
// QUESTION:
//   Determine if a binary tree is a valid BST.
// =============================================================
class N{constructor(v,l=null,r=null){this.v=v;this.l=l;this.r=r;}}
function isValidBST(n,lo=-Infinity,hi=Infinity){if(!n)return true;if(!(n.v>lo&&n.v<hi))return false;return isValidBST(n.l,lo,n.v)&&isValidBST(n.r,n.v,hi);}
console.log(isValidBST(new N(2,new N(1),new N(3))));
console.log(isValidBST(new N(5,new N(1),new N(4,new N(3),new N(6)))));
