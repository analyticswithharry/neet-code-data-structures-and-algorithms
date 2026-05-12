// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 093 -- Alien Dictionary
// Category   : Advanced Graphs
// Difficulty : Hard
// Study Plan : Day 47
// =============================================================
//
// QUESTION:
//   Given a sorted list of words from an alien language, derive the order of letters. Return any valid order or '' if impossible.
// =============================================================

var alienOrder = function(words){
  const g={}, ind={};
  for (const w of words) for (const c of w){ g[c]=g[c]||new Set(); ind[c]=ind[c]||0; }
  for (let i=0;i<words.length-1;i++){
    const a=words[i], b=words[i+1]; let found=false;
    const m=Math.min(a.length,b.length);
    for (let j=0;j<m;j++){
      if (a[j]!==b[j]){
        if (!g[a[j]].has(b[j])){ g[a[j]].add(b[j]); ind[b[j]]++; }
        found=true; break;
      }
    }
    if (!found && a.length>b.length) return "";
  }
  const q=[]; for (const c in ind) if (ind[c]===0) q.push(c);
  const res=[];
  while (q.length){
    const c=q.shift(); res.push(c);
    for (const nx of g[c]){ ind[nx]--; if (ind[nx]===0) q.push(nx); }
  }
  return res.length===Object.keys(ind).length ? res.join("") : "";
};
console.log(alienOrder(["wrt","wrf","er","ett","rftt"]));
