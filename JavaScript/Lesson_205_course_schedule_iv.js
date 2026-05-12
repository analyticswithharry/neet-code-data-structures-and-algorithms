// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 205 -- Course Schedule IV
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 103
// =============================================================
//
// QUESTION:
//   Given prerequisites, answer queries: is course u a (transitive) prerequisite of v?
// =============================================================
function checkIfPrerequisite(n,pre,queries){const r=Array.from({length:n},()=>new Array(n).fill(false));const g=Array.from({length:n},()=>[]);const ind=new Array(n).fill(0);for(const [a,b] of pre){g[a].push(b);ind[b]++;r[a][b]=true;}const q=[];for(let i=0;i<n;i++)if(ind[i]===0)q.push(i);const order=[];while(q.length){const x=q.shift();order.push(x);for(const y of g[x])if(--ind[y]===0)q.push(y);}for(const x of order)for(const y of g[x])for(let k=0;k<n;k++)if(r[k][x])r[k][y]=true;return queries.map(([u,v])=>r[u][v]);}
console.log(checkIfPrerequisite(3,[[1,2],[1,0],[2,0]],[[1,0],[1,2]]));
