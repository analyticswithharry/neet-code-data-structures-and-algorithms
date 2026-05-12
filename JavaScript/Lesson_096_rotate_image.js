// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 096 -- Rotate Image
// Category   : Math and Geometry
// Difficulty : Medium
// Study Plan : Day 48
// =============================================================
//
// QUESTION:
//   Rotate an n x n 2D matrix 90 degrees clockwise in-place.
// =============================================================

var rotate = function(m){
  const n=m.length;
  for (let i=0;i<n;i++) for (let j=i+1;j<n;j++) [m[i][j], m[j][i]]=[m[j][i], m[i][j]];
  for (const r of m) r.reverse();
};
const m=[[1,2,3],[4,5,6],[7,8,9]]; rotate(m); console.log(JSON.stringify(m));
