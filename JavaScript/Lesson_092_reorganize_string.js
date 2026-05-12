// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 092 -- Reorganize String
// Category   : Heap Priority Queue
// Difficulty : Medium
// Study Plan : Day 46
// =============================================================
//
// QUESTION:
//   Given a string s, rearrange so no two adjacent chars are equal. Return the rearranged string, or '' if impossible.
// =============================================================

var reorganizeString = function(s){
  const c={}; for (const ch of s) c[ch]=(c[ch]||0)+1;
  const n=s.length; let mx=0; for (const k in c) mx=Math.max(mx,c[k]);
  if (mx > Math.floor((n+1)/2)) return "";
  const arr=Object.entries(c).sort((a,b)=>b[1]-a[1]);
  const res=Array(n);
  let i=0;
  for (const [ch,cnt] of arr){
    for (let k=0;k<cnt;k++){
      if (i>=n) i=1;
      res[i]=ch; i+=2;
    }
  }
  return res.join("");
};
console.log(reorganizeString("aab"), JSON.stringify(reorganizeString("aaab")));
