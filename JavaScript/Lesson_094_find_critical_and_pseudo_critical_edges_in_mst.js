// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 094 -- Find Critical and Pseudo Critical Edges in MST
// Category   : Advanced Graphs
// Difficulty : Hard
// Study Plan : Day 47
// =============================================================
//
// QUESTION:
//   Given n nodes and weighted edges, find indices of critical and pseudo-critical edges in any MST.
// =============================================================

class DSU{ constructor(n){this.p=Array(n).fill(0).map((_,i)=>i); this.r=Array(n).fill(0); this.cnt=n;}
  f(x){ while(this.p[x]!==x){this.p[x]=this.p[this.p[x]]; x=this.p[x];} return x; }
  u(a,b){ a=this.f(a); b=this.f(b); if(a===b) return false;
    if(this.r[a]<this.r[b]){[a,b]=[b,a];} this.p[b]=a;
    if(this.r[a]===this.r[b]) this.r[a]++; this.cnt--; return true;}
}
var findCriticalAndPseudoCriticalEdges = function(n, edges){
  edges.forEach((e,i)=>e.push(i));
  edges.sort((a,b)=>a[2]-b[2]);
  const k=(skip=-1,force=-1)=>{
    const d=new DSU(n); let w=0;
    if (force>=0){ const [u,v,wt]=edges[force]; if(!d.u(u,v)) return Infinity; w+=wt; }
    for (let i=0;i<edges.length;i++){ if(i===skip) continue; const [u,v,wt]=edges[i]; if(d.u(u,v)) w+=wt; }
    return d.cnt===1 ? w : Infinity;
  };
  const base=k(); const crit=[], pseu=[];
  for (let i=0;i<edges.length;i++){
    if (k(i,-1) > base) crit.push(edges[i][3]);
    else if (k(-1,i) === base) pseu.push(edges[i][3]);
  }
  return [crit, pseu];
};
console.log(JSON.stringify(findCriticalAndPseudoCriticalEdges(5, [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]])));
