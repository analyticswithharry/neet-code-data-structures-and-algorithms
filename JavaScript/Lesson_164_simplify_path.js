// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 164 -- Simplify Path
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 82
// =============================================================
//
// QUESTION:
//   Given a Unix-style absolute path, return the simplified canonical path.
// =============================================================
function simplify(p){const st=[];for(const part of p.split('/')){if(part===''||part==='.')continue;if(part==='..'){if(st.length)st.pop();}else st.push(part);}return '/'+st.join('/');}
console.log(simplify("/a/./b/../../c/"));console.log(simplify("/home//foo/"));
