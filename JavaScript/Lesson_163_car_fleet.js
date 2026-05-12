// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 163 -- Car Fleet
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 82
// =============================================================
//
// QUESTION:
//   Cars at positions head to target with given speeds. Cars cannot pass; slower car ahead caps faster car behind. Return number of fleets that arrive.
// =============================================================
function carFleet(target,pos,sp){const cars=pos.map((p,i)=>[p,sp[i]]).sort((a,b)=>b[0]-a[0]);let f=0,lt=0;for(const [p,s] of cars){const t=(target-p)/s;if(t>lt){f++;lt=t;}}return f;}
console.log(carFleet(12,[10,8,0,5,3],[2,4,1,1,3]));
