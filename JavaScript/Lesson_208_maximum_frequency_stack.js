// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 208 -- Maximum Frequency Stack
// Category   : Stack
// Difficulty : Hard
// Study Plan : Day 104
// =============================================================
//
// QUESTION:
//   Push/pop a stack returning the most-frequent element (ties: most recent).
// =============================================================
class FreqStack{constructor(){this.f=new Map();this.g=new Map();this.maxf=0;}push(v){const c=(this.f.get(v)||0)+1;this.f.set(v,c);if(c>this.maxf)this.maxf=c;if(!this.g.has(c))this.g.set(c,[]);this.g.get(c).push(v);}pop(){const arr=this.g.get(this.maxf);const v=arr.pop();this.f.set(v,this.f.get(v)-1);if(arr.length===0)this.maxf--;return v;}}
const fs=new FreqStack();[5,7,5,7,4,5].forEach(x=>fs.push(x));console.log([fs.pop(),fs.pop(),fs.pop(),fs.pop()]);
