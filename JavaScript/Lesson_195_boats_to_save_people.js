// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 195 -- Boats to Save People
// Category   : Two Pointers
// Difficulty : Medium
// Study Plan : Day 98
// =============================================================
//
// QUESTION:
//   Each boat holds at most 2 people, total weight <= limit. Return min boats.
// =============================================================
function numRescueBoats(p,limit){p.sort((a,b)=>a-b);let i=0,j=p.length-1,b=0;while(i<=j){if(p[i]+p[j]<=limit)i++;j--;b++;}return b;}
console.log(numRescueBoats([3,2,2,1],3));console.log(numRescueBoats([3,5,3,4],5));
