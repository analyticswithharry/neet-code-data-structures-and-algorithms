// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 181 -- Open The Lock
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 91
// =============================================================
//
// QUESTION:
//   4-wheel lock starts at '0000'. Each move turns a wheel +/-1. Avoid deadends. Return min moves to reach target or -1.
// =============================================================
function openLock(dead,target){const D=new Set(dead);if(D.has("0000"))return -1;if(target==="0000")return 0;const seen=new Set(["0000"]);let q=[["0000",0]];while(q.length){const [s,d]=q.shift();for(let i=0;i<4;i++)for(const x of [-1,1]){const c=(parseInt(s[i])+x+10)%10;const ns=s.substring(0,i)+c+s.substring(i+1);if(ns===target)return d+1;if(!seen.has(ns)&&!D.has(ns)){seen.add(ns);q.push([ns,d+1]);}}}return -1;}
console.log(openLock(["0201","0101","0102","1212","2002"],"0202"));
