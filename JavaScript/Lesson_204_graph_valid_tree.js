// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 204 -- Graph Valid Tree
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 102
// =============================================================
//
// QUESTION:
//   Given n nodes and edges, determine if they form a tree (connected and no cycles).
// =============================================================
function validTree(n,edges){if(edges.length!==n-1)return false;const par=Array.from({length:n},(_,i)=>i);function find(x){while(par[x]!==x){par[x]=par[par[x]];x=par[x];}return x;}for(const [a,b] of edges){const ra=find(a),rb=find(b);if(ra===rb)return false;par[ra]=rb;}return true;}
console.log(validTree(5,[[0,1],[0,2],[0,3],[1,4]]));console.log(validTree(5,[[0,1],[1,2],[2,3],[1,3],[1,4]]));
