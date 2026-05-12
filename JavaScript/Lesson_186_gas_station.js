// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 186 -- Gas Station
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 93
// =============================================================
//
// QUESTION:
//   Gas[i]/cost[i] arrays around a circular route. Return start index to complete the circuit (or -1).
// =============================================================
function canCompleteCircuit(g,c){let s=0,t=0,tot=0;for(let i=0;i<g.length;i++){const d=g[i]-c[i];t+=d;tot+=d;if(t<0){s=i+1;t=0;}}return tot<0?-1:s;}
console.log(canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]));console.log(canCompleteCircuit([2,3,4],[3,4,3]));
