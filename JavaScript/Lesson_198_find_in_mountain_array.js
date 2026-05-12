// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 198 -- Find in Mountain Array
// Category   : Binary Search
// Difficulty : Hard
// Study Plan : Day 99
// =============================================================
//
// QUESTION:
//   Mountain array: strictly increasing then strictly decreasing. Return min index with value=target.
// =============================================================
function findInMountainArray(target,a){let lo=0,hi=a.length-1;while(lo<hi){const m=(lo+hi)>>1;if(a[m]<a[m+1])lo=m+1;else hi=m;}const peak=lo;function bs(l,r,asc){while(l<=r){const m=(l+r)>>1;if(a[m]===target)return m;if(asc){if(a[m]<target)l=m+1;else r=m-1;}else{if(a[m]>target)l=m+1;else r=m-1;}}return -1;}const i=bs(0,peak,true);return i!==-1?i:bs(peak+1,a.length-1,false);}
console.log(findInMountainArray(3,[1,2,3,4,5,3,1]));
