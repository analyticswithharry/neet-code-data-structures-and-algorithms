// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 192 -- Word Break II
// Category   : Backtracking
// Difficulty : Hard
// Study Plan : Day 96
// =============================================================
//
// QUESTION:
//   Return all sentences obtainable by segmenting s using words from dict.
// =============================================================
function wordBreak(s,wd){const w=new Set(wd),memo=new Map();function dfs(i){if(i===s.length)return [""];if(memo.has(i))return memo.get(i);const out=[];for(let j=i+1;j<=s.length;j++){const part=s.substring(i,j);if(w.has(part))for(const t of dfs(j))out.push(part+(t?" "+t:""));}memo.set(i,out);return out;}return dfs(0);}
console.log(wordBreak("catsanddog",["cat","cats","and","sand","dog"]));
