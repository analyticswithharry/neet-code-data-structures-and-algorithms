// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 090 -- Swim In Rising Water
// Category   : Advanced Graphs
// Difficulty : Hard
// Study Plan : Day 45
// =============================================================
//
// QUESTION:
//   On an n x n grid, grid[i][j] is the elevation. You start at (0,0) and want to reach (n-1,n-1). At time t the water level is t and you can move to a 4-neighbor cell if both are <= t. Return the minimum t.
// =============================================================

class MinHeap{ constructor(){this.a=[];} push(x){this.a.push(x); this._up(this.a.length-1);}
  pop(){const t=this.a[0],l=this.a.pop(); if(this.a.length){this.a[0]=l; this._dn(0);} return t;}
  size(){return this.a.length;}
  _up(i){while(i>0){const p=(i-1)>>1; if(this.a[p][0]>this.a[i][0]){[this.a[p],this.a[i]]=[this.a[i],this.a[p]]; i=p;} else break;}}
  _dn(i){const n=this.a.length; while(true){let l=2*i+1,r=2*i+2,s=i;
    if(l<n&&this.a[l][0]<this.a[s][0])s=l; if(r<n&&this.a[r][0]<this.a[s][0])s=r;
    if(s===i)break; [this.a[s],this.a[i]]=[this.a[i],this.a[s]]; i=s;}}
}
var swimInWater = function(grid){
  const n=grid.length; const h=new MinHeap(); h.push([grid[0][0],0,0]);
  const seen=new Set(["0,0"]); let ans=0;
  const dirs=[[1,0],[-1,0],[0,1],[0,-1]];
  while (h.size()){
    const [v,r,c]=h.pop(); ans=Math.max(ans,v);
    if (r===n-1 && c===n-1) return ans;
    for (const [dr,dc] of dirs){
      const nr=r+dr,nc=c+dc; const k=nr+","+nc;
      if (nr>=0&&nr<n&&nc>=0&&nc<n&&!seen.has(k)){ seen.add(k); h.push([grid[nr][nc],nr,nc]); }
    }
  } return -1;
};
console.log(swimInWater([[0,2],[1,3]]));
