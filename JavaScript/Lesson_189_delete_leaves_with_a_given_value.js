// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 189 -- Delete Leaves With a Given Value
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 95
// =============================================================
//
// QUESTION:
//   Delete all leaf nodes with a given target value (cascade).
// =============================================================
class N{constructor(v,l=null,r=null){this.v=v;this.l=l;this.r=r;}}
function removeLeafNodes(n,t){if(!n)return null;n.l=removeLeafNodes(n.l,t);n.r=removeLeafNodes(n.r,t);if(!n.l&&!n.r&&n.v===t)return null;return n;}
function out(n){if(!n)return null;return [n.v,out(n.l),out(n.r)];}
console.log(JSON.stringify(out(removeLeafNodes(new N(1,new N(2,new N(2)),new N(3,new N(2),new N(4))),2))));
