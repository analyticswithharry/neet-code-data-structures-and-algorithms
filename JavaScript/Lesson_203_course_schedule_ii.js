// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 203 -- Course Schedule II
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 102
// =============================================================
//
// QUESTION:
//   Return any topological ordering of courses, or empty array if impossible.
// =============================================================
function findOrder(n,pre){const g=Array.from({length:n},()=>[]);const ind=new Array(n).fill(0);for(const [a,b] of pre){g[b].push(a);ind[a]++;}const q=[];for(let i=0;i<n;i++)if(ind[i]===0)q.push(i);const res=[];while(q.length){const x=q.shift();res.push(x);for(const y of g[x])if(--ind[y]===0)q.push(y);}return res.length===n?res:[];}
console.log(findOrder(4,[[1,0],[2,0],[3,1],[3,2]]));
