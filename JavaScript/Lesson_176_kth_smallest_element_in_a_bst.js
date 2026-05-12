// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 176 -- Kth Smallest Element In a Bst
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 88
// =============================================================
//
// QUESTION:
//   Return the kth smallest value in a BST (1-indexed).
// =============================================================
class N{constructor(v,l=null,r=null){this.v=v;this.l=l;this.r=r;}}
function kth(root,k){const st=[];let cur=root;while(cur||st.length){while(cur){st.push(cur);cur=cur.l;}cur=st.pop();if(--k===0)return cur.v;cur=cur.r;}}
const r=new N(3,new N(1,null,new N(2)),new N(4));
console.log(kth(r,1));console.log(kth(r,3));
