// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 103 -- Merge Intervals
// Category   : Intervals
// Difficulty : Medium
// Study Plan : Day 52
// =============================================================
//
// QUESTION:
//   Given an array of intervals where intervals[i] = [start, end], merge all overlapping intervals.
// =============================================================

var merge = function(intervals){
  intervals.sort((a,b)=>a[0]-b[0]);
  const res=[];
  for (const [s,e] of intervals){
    if (res.length && s<=res[res.length-1][1]) res[res.length-1][1]=Math.max(res[res.length-1][1], e);
    else res.push([s,e]);
  }
  return res;
};
console.log(JSON.stringify(merge([[1,3],[2,6],[8,10],[15,18]])));
