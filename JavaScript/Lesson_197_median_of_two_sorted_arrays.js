// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 197 -- Median of Two Sorted Arrays
// Category   : Binary Search
// Difficulty : Hard
// Study Plan : Day 99
// =============================================================
//
// QUESTION:
//   Find the median of the two sorted arrays in O(log(min(m,n))).
// =============================================================
function findMedianSortedArrays(a,b){if(a.length>b.length)[a,b]=[b,a];const m=a.length,n=b.length;let lo=0,hi=m;while(lo<=hi){const i=(lo+hi)>>1;const j=((m+n+1)>>1)-i;const Lx=i>0?a[i-1]:-Infinity,Rx=i<m?a[i]:Infinity,Ly=j>0?b[j-1]:-Infinity,Ry=j<n?b[j]:Infinity;if(Lx<=Ry&&Ly<=Rx){if((m+n)&1)return Math.max(Lx,Ly);return (Math.max(Lx,Ly)+Math.min(Rx,Ry))/2;}else if(Lx>Ry)hi=i-1;else lo=i+1;}}
console.log(findMedianSortedArrays([1,3],[2]));console.log(findMedianSortedArrays([1,2],[3,4]));
