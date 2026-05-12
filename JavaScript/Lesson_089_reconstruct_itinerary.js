// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 089 -- Reconstruct Itinerary
// Category   : Advanced Graphs
// Difficulty : Hard
// Study Plan : Day 45
// =============================================================
//
// QUESTION:
//   Given a list of airline tickets [from,to], reconstruct the itinerary in order, starting from 'JFK'. If multiple valid, return the lexicographically smallest one.
// =============================================================

var findItinerary = function(tickets){
  const g={}; for (const [a,b] of tickets){ (g[a]=g[a]||[]).push(b); }
  for (const k in g) g[k].sort().reverse();
  const st=["JFK"], res=[];
  while (st.length){
    while (g[st[st.length-1]] && g[st[st.length-1]].length) st.push(g[st[st.length-1]].pop());
    res.push(st.pop());
  }
  return res.reverse();
};
console.log(findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]));
