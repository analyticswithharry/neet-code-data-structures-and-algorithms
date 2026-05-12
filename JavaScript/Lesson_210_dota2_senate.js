// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 210 -- Dota2 Senate
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 105
// =============================================================
//
// QUESTION:
//   Senate string of 'R'/'D'. Each round senators ban earliest opponent. Return winning party.
// =============================================================
function predictPartyVictory(s){const R=[],D=[];const n=s.length;for(let i=0;i<n;i++)(s[i]==='R'?R:D).push(i);while(R.length&&D.length){const r=R.shift(),d=D.shift();if(r<d)R.push(r+n);else D.push(d+n);}return R.length?"Radiant":"Dire";}
console.log(predictPartyVictory("RD"));console.log(predictPartyVictory("RDD"));
