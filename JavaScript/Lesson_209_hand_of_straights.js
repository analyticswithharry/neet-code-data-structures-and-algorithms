// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 209 -- Hand of Straights
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 105
// =============================================================
//
// QUESTION:
//   Can hand be rearranged into groups of size W of consecutive cards?
// =============================================================
function isNStraightHand(h,W){if(h.length%W)return false;const c=new Map();for(const x of h)c.set(x,(c.get(x)||0)+1);const keys=[...c.keys()].sort((a,b)=>a-b);for(const x of keys){const cnt=c.get(x);if(cnt>0){for(let k=0;k<W;k++){const v=c.get(x+k)||0;if(v<cnt)return false;c.set(x+k,v-cnt);}}}return true;}
console.log(isNStraightHand([1,2,3,6,2,3,4,7,8],3));console.log(isNStraightHand([1,2,3,4,5],4));
