// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 206 -- Number of Connected Components In An Undirected Graph
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 103
// =============================================================
//
// QUESTION:
//   Given n nodes and undirected edges, return the number of connected components.
// =============================================================
function countComponents(n,edges){const par=Array.from({length:n},(_,i)=>i);let cnt=n;function find(x){while(par[x]!==x){par[x]=par[par[x]];x=par[x];}return x;}for(const [a,b] of edges){const ra=find(a),rb=find(b);if(ra!==rb){par[ra]=rb;cnt--;}}return cnt;}
console.log(countComponents(5,[[0,1],[1,2],[3,4]]));
