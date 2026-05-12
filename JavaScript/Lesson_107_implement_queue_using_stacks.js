// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 107 -- Implement Queue using Stacks
// Category   : Stack
// Difficulty : Easy
// Study Plan : Day 54
// =============================================================
//
// QUESTION:
//   Implement a FIFO queue using only two stacks.
// =============================================================

class MyQueue {
  constructor(){ this.a=[]; this.b=[]; }
  push(x){ this.a.push(x); }
  pop(){ if (!this.b.length) while (this.a.length) this.b.push(this.a.pop()); return this.b.pop(); }
  peek(){ if (!this.b.length) while (this.a.length) this.b.push(this.a.pop()); return this.b[this.b.length-1]; }
  empty(){ return !this.a.length && !this.b.length; }
}
const q=new MyQueue(); q.push(1); q.push(2); console.log(q.peek(), q.pop(), q.empty());
