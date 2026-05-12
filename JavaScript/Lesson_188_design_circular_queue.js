// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 188 -- Design Circular Queue
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 94
// =============================================================
//
// QUESTION:
//   Implement a fixed-size circular queue with enQueue/deQueue/Front/Rear/isEmpty/isFull.
// =============================================================
class CQ{constructor(k){this.a=new Array(k);this.k=k;this.h=0;this.c=0;}enQueue(v){if(this.c===this.k)return false;this.a[(this.h+this.c)%this.k]=v;this.c++;return true;}deQueue(){if(!this.c)return false;this.h=(this.h+1)%this.k;this.c--;return true;}Front(){return this.c?this.a[this.h]:-1;}Rear(){return this.c?this.a[(this.h+this.c-1)%this.k]:-1;}isEmpty(){return this.c===0;}isFull(){return this.c===this.k;}}
const q=new CQ(3);console.log(q.enQueue(1),q.enQueue(2),q.enQueue(3),q.enQueue(4));console.log(q.Rear(),q.isFull(),q.deQueue(),q.enQueue(4),q.Rear());
