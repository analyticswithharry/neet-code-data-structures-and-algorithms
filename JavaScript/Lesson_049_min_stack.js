// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 049 -- Min Stack
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 24
// =============================================================
//
// QUESTION:
//   Design a stack supporting push, pop, top, and getMin in O(1).
// =============================================================

class MinStack {
    constructor(){ this.s=[]; this.m=[]; }
    push(v){ this.s.push(v); this.m.push(this.m.length?Math.min(v,this.m[this.m.length-1]):v); }
    pop(){ this.s.pop(); this.m.pop(); }
    top(){ return this.s[this.s.length-1]; }
    getMin(){ return this.m[this.m.length-1]; }
}
const s = new MinStack(); s.push(-2); s.push(0); s.push(-3);
console.log(s.getMin()); s.pop(); console.log(s.top()); console.log(s.getMin());
