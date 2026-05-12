// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 187 -- Reverse Linked List II
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 94
// =============================================================
//
// QUESTION:
//   Reverse the nodes of the list from position left to right (1-indexed).
// =============================================================
class N{constructor(v,n=null){this.v=v;this.n=n;}}
function reverseBetween(h,L,R){const d=new N(0,h);let pre=d;for(let i=0;i<L-1;i++)pre=pre.n;let cur=pre.n;for(let i=0;i<R-L;i++){const nxt=cur.n;cur.n=nxt.n;nxt.n=pre.n;pre.n=nxt;}return d.n;}
function fromList(a){const d=new N(0);let c=d;for(const x of a){c.n=new N(x);c=c.n;}return d.n;}
function toList(h){const r=[];while(h){r.push(h.v);h=h.n;}return r;}
console.log(toList(reverseBetween(fromList([1,2,3,4,5]),2,4)));
