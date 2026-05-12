// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 104 -- Non Overlapping Intervals
// Category   : Intervals
// Difficulty : Medium
// Study Plan : Day 52
// =============================================================
//
// QUESTION:
//   Given an array of intervals, return the minimum number of intervals to remove so the rest are non-overlapping.
// =============================================================

var eraseOverlapIntervals = function(intervals){
  intervals.sort((a,b)=>a[1]-b[1]); let end=-Infinity, rm=0;
  for (const [s,e] of intervals){ if (s>=end) end=e; else rm++; }
  return rm;
};
console.log(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]));
