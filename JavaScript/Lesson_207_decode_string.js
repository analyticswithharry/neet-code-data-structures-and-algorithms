// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 207 -- Decode String
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 104
// =============================================================
//
// QUESTION:
//   Decode a run-length-style string like "3[a2[c]]" -> "accaccacc".
// =============================================================
function decodeString(s){const st=[];let cur="",k=0;for(const ch of s){if(ch>='0'&&ch<='9')k=k*10+(ch.charCodeAt(0)-48);else if(ch==='['){st.push([cur,k]);cur="";k=0;}else if(ch===']'){const [pre,n]=st.pop();cur=pre+cur.repeat(n);}else cur+=ch;}return cur;}
console.log(decodeString("3[a]2[bc]"));console.log(decodeString("3[a2[c]]"));
