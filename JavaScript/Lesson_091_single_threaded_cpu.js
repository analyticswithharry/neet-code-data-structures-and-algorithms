// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 091 -- Single Threaded CPU
// Category   : Heap Priority Queue
// Difficulty : Medium
// Study Plan : Day 46
// =============================================================
//
// QUESTION:
//   You have tasks[i] = [enqueueTime, processingTime]. CPU picks the task with shortest processing time available; ties broken by index. Return order of indices.
// =============================================================

class MinHeap{ constructor(c){this.a=[];this.c=c;} size(){return this.a.length;}
  push(x){this.a.push(x);this._u(this.a.length-1);}
  pop(){const t=this.a[0],l=this.a.pop(); if(this.a.length){this.a[0]=l;this._d(0);} return t;}
  _u(i){while(i>0){const p=(i-1)>>1; if(this.c(this.a[p],this.a[i])>0){[this.a[p],this.a[i]]=[this.a[i],this.a[p]];i=p;}else break;}}
  _d(i){const n=this.a.length; while(true){let l=2*i+1,r=2*i+2,s=i;
    if(l<n&&this.c(this.a[l],this.a[s])<0)s=l; if(r<n&&this.c(this.a[r],this.a[s])<0)s=r;
    if(s===i)break; [this.a[s],this.a[i]]=[this.a[i],this.a[s]]; i=s;}}
}
var getOrder = function(tasks){
  const idx=tasks.map((_,i)=>i).sort((a,b)=>tasks[a][0]-tasks[b][0]);
  const h=new MinHeap((x,y)=>x[0]!==y[0]?x[0]-y[0]:x[1]-y[1]);
  let t=0,i=0; const res=[];
  while (i<idx.length || h.size()){
    if (!h.size()) t=Math.max(t, tasks[idx[i]][0]);
    while (i<idx.length && tasks[idx[i]][0]<=t){ h.push([tasks[idx[i]][1],idx[i]]); i++; }
    const [p,j]=h.pop(); t+=p; res.push(j);
  } return res;
};
console.log(getOrder([[1,2],[2,4],[3,2],[4,1]]));
