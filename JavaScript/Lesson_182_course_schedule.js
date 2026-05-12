// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 182 -- Course Schedule
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 91
// =============================================================
//
// QUESTION:
//   Given prerequisites pairs, can all courses be finished (no cycle)?
// =============================================================
function canFinish(n,pre){const g=Array.from({length:n},()=>[]);const ind=new Array(n).fill(0);for(const [a,b] of pre){g[b].push(a);ind[a]++;}const q=[];for(let i=0;i<n;i++)if(ind[i]===0)q.push(i);let cnt=0;while(q.length){const x=q.shift();cnt++;for(const y of g[x])if(--ind[y]===0)q.push(y);}return cnt===n;}
console.log(canFinish(2,[[1,0]]));console.log(canFinish(2,[[1,0],[0,1]]));
