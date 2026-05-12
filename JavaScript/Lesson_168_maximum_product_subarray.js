// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 168 -- Maximum Product Subarray
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 84
// =============================================================
//
// QUESTION:
//   Find a contiguous subarray with the largest product.
// =============================================================
function maxProduct(a){let mx=a[0],mn=a[0],res=a[0];for(let i=1;i<a.length;i++){const v=a[i];if(v<0){[mx,mn]=[mn,mx];}mx=Math.max(v,mx*v);mn=Math.min(v,mn*v);res=Math.max(res,mx);}return res;}
console.log(maxProduct([2,3,-2,4]));console.log(maxProduct([-2,0,-1]));
